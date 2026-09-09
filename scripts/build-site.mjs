import { cp, mkdir, readFile, rm, stat, writeFile } from "node:fs/promises";
import { createWriteStream } from "node:fs";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";
import archiver from "archiver";
import { marked } from "marked";

const here = path.dirname(fileURLToPath(import.meta.url));
const publication = path.resolve(here, "..");
const contentRoot = path.join(publication, "content");
const publicRoot = path.join(publication, "public");
const outputRoot = path.join(publication, "dist");
const isCheck = process.argv.includes("--check");

const architectures = [
  { key: "01-secure-business-ai", number: "01", title: "Secure business AI", question: "What may our AI access and do?", image: "01-secure-business-ai.png" },
  { key: "02-defend-against-ai", number: "02", title: "Defend against AI", question: "How do we stop AI-enabled attacks?", image: "02-defend-against-ai.png" },
  { key: "03-defend-with-ai", number: "03", title: "Defend with AI", question: "How can AI help security act within limits?", image: "03-defend-with-ai.png" }
];

const pages = [
  { slug: "sources", source: "sources.md", title: "Sources", section: "Sources" },
  { slug: "review-status", source: "review-status.md", title: "Review status", section: "Review status", review: true },
  { slug: "authoring-standard", source: "authoring-standard.md", title: "Authoring standard", section: "Authoring standard" },
  { slug: "source-map", source: "source-map.md", title: "Source map", section: "Source map" },
  { slug: "guides", source: "guide-index.md", title: "Architect guides", section: "Architect guides" },
  { slug: "templates/reference-architecture", source: "templates/reference-architecture.md", title: "Reference architecture template", section: "Reference architecture template" }
];

const requiredFiles = [
  "00-ai-security.md",
  ...architectures.map((architecture) => `${architecture.key}.md`),
  ...architectures.map((architecture) => `guides/${architecture.key}-guide.md`),
  ...pages.map((page) => page.source),
  ...["00-ai-security.png", ...architectures.map((architecture) => architecture.image)].map((image) => `images/${image}`)
];

const escapeHtml = (value) => String(value)
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;")
  .replaceAll("'", "&#39;");

function pagePath(relative) {
  return `/${relative.replace(/^\//, "").replace(/index\.html$/, "")}`.replace(/\/$/, "") || "/";
}

function hrefFrom(sourcePage, target) {
  if (!target || target.startsWith("#") || /^[a-z][a-z0-9+.-]*:/i.test(target)) return target;
  const [rawPath, fragment] = target.split("#");
  const names = {
    "00-ai-security.md": "/",
    "01-secure-business-ai.md": "/architectures/01-secure-business-ai",
    "02-defend-against-ai.md": "/architectures/02-defend-against-ai",
    "03-defend-with-ai.md": "/architectures/03-defend-with-ai",
    "sources.md": "/sources",
    "review-status.md": "/review-status",
    "authoring-standard.md": "/authoring-standard",
    "source-map.md": "/source-map",
    "guide-index.md": "/guides",
    "templates/reference-architecture.md": "/templates/reference-architecture",
    "guides/01-secure-business-ai-guide.md": "/guides/01-secure-business-ai-guide",
    "guides/02-defend-against-ai-guide.md": "/guides/02-defend-against-ai-guide",
    "guides/03-defend-with-ai-guide.md": "/guides/03-defend-with-ai-guide"
  };
  const normalized = path.posix.normalize(path.posix.join(path.posix.dirname(sourcePage), rawPath));
  if (/\.png$/i.test(rawPath)) return `/images/${path.posix.basename(normalized)}${fragment ? `#${slugify(fragment)}` : ""}`;
  const href = names[normalized] ?? names[rawPath] ?? rawPath;
  return fragment ? `${href}#${slugify(fragment)}` : href;
}

function slugify(value) {
  return String(value).toLowerCase().trim().replace(/<[^>]+>/g, "").replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
}

function plainText(markdown) {
  return markdown
    .replace(/^#{1,6}\s+/gm, "")
    .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1")
    .replace(/[>*_`]/g, "")
    .replace(/\n+/g, " ")
    .trim();
}

function metadata(markdown, fallbackTitle) {
  const title = markdown.match(/^#\s+(.+)$/m)?.[1] ?? fallbackTitle;
  const status = markdown.match(/\bStatus:\s*([^\n]+)/i)?.[1]?.trim();
  const version = markdown.match(/\bVersion:\s*([^·\n]+)/i)?.[1]?.trim();
  return { title, status, version };
}

function renderMarkdown(markdown, sourcePage) {
  const renderer = new marked.Renderer();
  renderer.heading = ({ text, depth }) => `<h${depth} id="${slugify(text)}">${text}</h${depth}>`;
  renderer.link = ({ href, title, text }) => {
    const destination = hrefFrom(sourcePage, href);
    const external = /^[a-z][a-z0-9+.-]*:/i.test(destination);
    const annotation = title ? ` title="${escapeHtml(title)}"` : "";
    const target = external ? ' target="_blank" rel="noreferrer"' : "";
    return `<a href="${escapeHtml(destination)}"${annotation}${target}>${text}</a>`;
  };
  renderer.image = ({ href, title, text }) => {
    const imagePath = /^[a-z][a-z0-9+.-]*:/i.test(href)
      ? href
      : `/images/${path.posix.basename(path.posix.normalize(path.posix.join(path.posix.dirname(sourcePage), href)))}`;
    const annotation = title ? ` title="${escapeHtml(title)}"` : "";
    return `<img src="${escapeHtml(imagePath)}" alt="${escapeHtml(text || "")}"${annotation} loading="lazy">`;
  };
  return marked.parse(markdown, { gfm: true, renderer, mangle: false, headerIds: false });
}

function toc(markdown) {
  const entries = [...markdown.matchAll(/^(#{2,3})\s+(.+)$/gm)].map((match) => ({
    level: match[1].length,
    text: match[2].replace(/[*_`]/g, ""),
    id: slugify(match[2])
  }));
  if (entries.length < 2) return "";
  return `<nav class="article-toc" aria-label="On this page"><span>On this page</span><ol>${entries.map((entry) => `<li class="toc-level-${entry.level}"><a href="#${entry.id}">${entry.text}</a></li>`).join("")}</ol></nav>`;
}

function nav(active = "") {
  const item = (href, label, id) => `<a href="${href}"${active === id ? ' aria-current="page"' : ""}>${label}</a>`;
  return `<header class="site-header"><div class="site-header-inner"><a class="wordmark" href="/" aria-label="AI Security Reference Architectures home"><span>AI security</span><span>reference architectures</span></a><button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button><nav id="site-nav" class="site-nav" aria-label="Primary navigation">${item("/", "Overview", "overview")}<div class="nav-menu"><button type="button" aria-expanded="false">Architectures</button><div class="nav-menu-panel">${architectures.map((architecture) => `<a href="/architectures/${architecture.key}"><b>${architecture.number}</b>${architecture.title}</a>`).join("")}</div></div>${item("/sources", "Sources", "sources")}${item("/review-status", "Review status", "review")}${item("/authoring-standard", "Authoring standard", "standard")}</nav></div></header>`;
}

function footer() {
  return `<footer class="site-footer"><div><a class="wordmark wordmark-footer" href="/"><span>AI security</span><span>reference architectures</span></a><p>Discussion drafts for security and architecture conversations.</p></div><div class="footer-links"><a href="https://github.com/jessepike/ai-security-reference-architectures" target="_blank" rel="noreferrer">GitHub</a><a href="mailto:jesse@jessepike.dev?subject=AI%20Security%20Reference%20Architectures%20feedback">Send feedback</a></div></footer>`;
}

function layout({ title, description, active, main, bodyClass = "", canonicalPath = "/", socialImage = "/images/00-ai-security.png" }) {
  const canonicalUrl = `https://ai.jessepike.dev${canonicalPath}`;
  const socialImageUrl = `https://ai.jessepike.dev${socialImage}`;
  const fullTitle = `${title} · AI Security Reference Architectures`;
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="${escapeHtml(description)}"><meta name="theme-color" content="#092a43"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="canonical" href="${canonicalUrl}"><meta property="og:type" content="website"><meta property="og:site_name" content="AI Security Reference Architectures"><meta property="og:title" content="${escapeHtml(fullTitle)}"><meta property="og:description" content="${escapeHtml(description)}"><meta property="og:url" content="${canonicalUrl}"><meta property="og:image" content="${socialImageUrl}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="${escapeHtml(fullTitle)}"><meta name="twitter:description" content="${escapeHtml(description)}"><meta name="twitter:image" content="${socialImageUrl}"><title>${escapeHtml(fullTitle)}</title><link rel="stylesheet" href="/assets/site.css"></head><body class="${bodyClass}"><a class="skip-link" href="#main-content">Skip to content</a>${nav(active)}<main id="main-content">${main}</main>${footer()}<dialog class="image-dialog" aria-label="Expanded architecture image"><button class="image-dialog-close" type="button" aria-label="Close full-size image">Close</button><img alt=""></dialog><script src="/assets/site.js" defer></script></body></html>`;
}

function feedbackLink(subject) {
  return `mailto:jesse@jessepike.dev?subject=${encodeURIComponent(subject)}`;
}

function imageFigure(image, alt, caption) {
  return `<figure class="architecture-figure"><button class="architecture-image-button" type="button" data-full-image="/images/${image}" data-full-alt="${escapeHtml(alt)}" aria-label="Open ${escapeHtml(caption)} at full size"><img src="/images/${image}" alt="${escapeHtml(alt)}" width="1672" height="941"></button><figcaption>${caption}<button class="text-link" type="button" data-full-image="/images/${image}" data-full-alt="${escapeHtml(alt)}">View full size</button></figcaption></figure>`;
}

function downloadLinks(architecture) {
  const fileBase = architecture.key;
  return `<aside class="download-panel" aria-label="Downloads"><h2>Downloads</h2><a href="/downloads/${fileBase}.png" download>Architecture PNG</a><a href="/downloads/${fileBase}.md" download>Source architecture Markdown</a><a href="/downloads/${fileBase}-guide.md" download>Architect guide Markdown</a><a href="/downloads/${fileBase}-guide.pdf" download>Architect guide PDF</a><a href="/downloads/ai-security-reference-architectures.zip" download>Clean reference package</a><a href="/downloads/ai-security-reference-architectures.pptx" download>Editable PowerPoint</a></aside>`;
}

async function exists(file) {
  try { await stat(file); return true; } catch { return false; }
}

async function assertInputs() {
  const missing = [];
  for (const relative of requiredFiles) if (!await exists(path.join(relative.startsWith("images/") ? publicRoot : contentRoot, relative))) missing.push(relative);
  for (const page of pages.slice(3)) if (!await exists(path.join(contentRoot, page.source))) missing.push(page.source);
  if (!await exists(path.join(publicRoot, "downloads", "ai-security-reference-architectures.pptx"))) {
    console.warn("Note: editable PowerPoint is not present yet; its download link will remain in the site.");
  }
  if (missing.length) throw new Error(`Cannot build the public site. Missing publication inputs:\n${missing.map((file) => `  - ${file}`).join("\n")}`);
}

async function readContent(relative) { return readFile(path.join(contentRoot, relative), "utf8"); }

async function writeOutput(relative, html) {
  const destination = path.join(outputRoot, relative);
  await mkdir(path.dirname(destination), { recursive: true });
  await writeFile(destination, html);
}

async function archiveCleanPackage() {
  const destination = path.join(outputRoot, "downloads", "ai-security-reference-architectures.zip");
  await mkdir(path.dirname(destination), { recursive: true });
  await new Promise((resolve, reject) => {
    const archive = archiver("zip", { zlib: { level: 9 } });
    const stream = createWriteStream(destination);
    archive.on("error", reject);
    stream.on("close", resolve);
    archive.pipe(stream);
    archive.file(path.join(publication, "README.md"), { name: "README.md" });
    archive.glob("**/*.md", { cwd: contentRoot }, { prefix: "content" });
    archive.glob("**/*.png", { cwd: path.join(publicRoot, "images") }, { prefix: "public/images" });
    archive.glob("**/*.pdf", { cwd: path.join(publicRoot, "downloads") }, { prefix: "public/downloads" });
    archive.glob("**/*.pptx", { cwd: path.join(publicRoot, "downloads") }, { prefix: "public/downloads" });
    archive.finalize();
  });
}

async function build() {
  await assertInputs();
  await rm(outputRoot, { recursive: true, force: true });
  await mkdir(outputRoot, { recursive: true });
  await cp(publicRoot, outputRoot, { recursive: true });
  await mkdir(path.join(outputRoot, "assets"), { recursive: true });
  await cp(path.join(publication, "site"), path.join(outputRoot, "assets"), { recursive: true });

  const overview = await readContent("00-ai-security.md");
  const overviewMeta = metadata(overview, "AI Security");
  const story = overview.match(/^## The story\s*\n([\s\S]*?)(?=^## )/m)?.[1] ?? overview;
  const opening = plainText(story).slice(0, 340).replace(/\s+\S*$/, "…");
  const overviewPage = `<section class="hero hero-overview"><div class="hero-copy"><p class="kicker">A library for the security conversation around AI</p><h1>${overviewMeta.title}</h1><p class="hero-statement">AI changes what we protect, how we are attacked, and how we defend.</p><p class="hero-intro">${escapeHtml(opening)}</p><div class="hero-actions"><a class="button button-primary" href="#the-overview">Read the overview</a><a class="button button-secondary" href="/downloads/ai-security-reference-architectures.pptx" download>Download the presentation</a><a class="button button-secondary" href="/architectures/01-secure-business-ai">Start with secure business AI</a></div></div><div class="hero-visual">${imageFigure("00-ai-security.png", "Overview of the three AI security reference architectures and their shared foundation.", "Series overview · proposed v0.1")}</div></section><section class="architecture-index" aria-labelledby="architecture-index-title"><div class="section-heading"><p class="kicker">Three views of one security program</p><h2 id="architecture-index-title">Choose the question you need to answer.</h2></div><div class="architecture-grid">${architectures.map((architecture) => `<article class="architecture-card"><div><span class="architecture-number">${architecture.number}</span><h3>${architecture.title}</h3><p>${architecture.question}</p></div><div class="card-actions"><a href="/architectures/${architecture.key}" aria-label="Read ${architecture.title}">Read the architecture</a><a href="/downloads/${architecture.key}-guide.pdf" download>Guide PDF</a></div></article>`).join("")}</div></section><section id="the-overview" class="article-section article-section-overview"><div class="article-frame"><aside>${toc(overview)}</aside><article class="prose">${renderMarkdown(overview, "00-ai-security.md")}</article></div></section>`;
  await writeOutput("index.html", layout({ title: "AI Security", description: "Public discussion drafts that frame AI security as secure business AI, defense against AI-enabled attacks, and defense with AI.", active: "overview", main: overviewPage, bodyClass: "overview-page", canonicalPath: "/" }));

  for (const architecture of architectures) {
    const markdown = await readContent(`${architecture.key}.md`);
    const guide = await readContent(`guides/${architecture.key}-guide.md`);
    const info = metadata(markdown, architecture.title);
    const architecturePage = `<section class="architecture-hero"><div><p class="kicker">Reference architecture ${architecture.number}</p><h1>${info.title}</h1><p class="architecture-question">${architecture.question}</p><div class="meta-row">${info.version ? `<span>${escapeHtml(info.version)}</span>` : ""}${info.status ? `<span>${escapeHtml(info.status)}</span>` : ""}</div></div>${imageFigure(architecture.image, `${architecture.title} reference architecture.`, `${architecture.title} · discussion draft`)}</section><section class="article-section"><div class="article-frame"><aside>${toc(markdown)}${downloadLinks(architecture)}<a class="feedback-link" href="${feedbackLink(`Feedback on ${architecture.number}: ${architecture.title}`)}">Share feedback on this architecture</a></aside><article class="prose">${renderMarkdown(markdown, `${architecture.key}.md`)}<hr><p class="article-next"><a href="/guides/${architecture.key}-guide">Read the detailed architect guide</a></p></article></div></section>`;
    await writeOutput(`architectures/${architecture.key}.html`, layout({ title: architecture.title, description: architecture.question, active: "architectures", main: architecturePage, bodyClass: "architecture-page", canonicalPath: `/architectures/${architecture.key}`, socialImage: `/images/${architecture.image}` }));
    const guidePage = `<section class="document-hero"><p class="kicker">Detailed architect guide</p><h1>${architecture.title}</h1><p>The image is a sparse companion. This guide explains the design, interfaces, decisions, limits, and evidence in the source.</p><div class="document-actions"><a class="button button-secondary" href="/architectures/${architecture.key}">View the architecture</a><a class="button button-secondary" href="/downloads/${architecture.key}-guide.md" download>Download guide Markdown</a><a class="button button-secondary" href="/downloads/${architecture.key}-guide.pdf" download>Download guide PDF</a></div></section><section class="article-section"><div class="article-frame"><aside>${toc(guide)}<a class="feedback-link" href="${feedbackLink(`Feedback on ${architecture.number} guide: ${architecture.title}`)}">Share feedback on this guide</a></aside><article class="prose prose-guide">${renderMarkdown(guide, `guides/${architecture.key}-guide.md`)}</article></div></section>`;
    await writeOutput(`guides/${architecture.key}-guide.html`, layout({ title: `${architecture.title} guide`, description: `Detailed guide for the ${architecture.title} AI security reference architecture.`, active: "architectures", main: guidePage, bodyClass: "guide-page", canonicalPath: `/guides/${architecture.key}-guide`, socialImage: `/images/${architecture.image}` }));
  }

  for (const page of pages) {
    const markdown = await readContent(page.source);
    const pageMeta = metadata(markdown, page.title);
    const callout = page.review ? `<aside class="status-callout"><p>Discussion draft</p><p>The component architecture packages received model-assisted review with material reservations. Open findings are preserved in this public summary. The overview and authoring standard have not received model-assisted review.</p></aside>` : "";
    const genericPage = `<section class="document-hero"><p class="kicker">${page.section}</p><h1>${pageMeta.title}</h1>${pageMeta.status ? `<p class="document-status">${escapeHtml(pageMeta.status)}</p>` : ""}</section><section class="article-section"><div class="article-frame"><aside>${toc(markdown)}<a class="feedback-link" href="${feedbackLink(`Feedback on AI Security Reference Architectures: ${page.title}`)}">Send feedback</a></aside><article class="prose">${callout}${renderMarkdown(markdown, page.source)}</article></div></section>`;
    await writeOutput(`${page.slug}.html`, layout({ title: page.title, description: `${page.title} for the AI Security Reference Architectures publication.`, active: page.review ? "review" : page.slug, main: genericPage, bodyClass: "document-page", canonicalPath: `/${page.slug}` }));
  }

  const downloadMap = [
    ["00-ai-security.md", "00-ai-security.md"],
    ...architectures.flatMap((architecture) => [
      [`${architecture.key}.md`, `${architecture.key}.md`],
      [`guides/${architecture.key}-guide.md`, `${architecture.key}-guide.md`]
    ])
  ];
  for (const [source, destination] of downloadMap) await cp(path.join(contentRoot, source), path.join(outputRoot, "downloads", destination));
  for (const architecture of architectures) {
    const pdf = `${architecture.key}-guide.pdf`;
    const sourcePdf = path.join(publicRoot, "downloads", pdf);
    if (await exists(sourcePdf)) await cp(sourcePdf, path.join(outputRoot, "downloads", pdf));
  }
  for (const image of ["00-ai-security.png", ...architectures.map((architecture) => architecture.image)]) await cp(path.join(publicRoot, "images", image), path.join(outputRoot, "downloads", image));
  await archiveCleanPackage();
  console.log(`Built ${outputRoot}`);
}

if (isCheck) {
  await assertInputs();
  console.log("Publication inputs are present.");
} else {
  await build();
}
