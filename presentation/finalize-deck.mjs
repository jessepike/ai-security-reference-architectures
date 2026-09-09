import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";

const workspaceDir = process.env.WORKSPACE_DIR ?? process.cwd();
const skillDir = process.env.SKILL_DIR;
const pythonExecutable = process.env.RUNTIME_PYTHON ?? "/usr/bin/python3";
const candidatePath = path.join(workspaceDir, "tmp/presentation/ai-security-reference-architectures.candidate.pptx");
const finalPath = path.join(workspaceDir, "output/pptx/ai-security-reference-architectures.pptx");
const stagingDir = path.join(workspaceDir, "tmp/presentation/finalizer");
await fs.mkdir(stagingDir, { recursive: true });
await fs.mkdir(path.dirname(finalPath), { recursive: true });
const { finalizePresentation } = await import(pathToFileURL(
  path.join(skillDir, "container_tools/artifact_tool_utils.mjs"),
).href);
const result = await finalizePresentation({
  workspaceDir,
  candidatePath,
  finalPath,
  pythonExecutable,
  integrityValidatorPath: path.join(skillDir, "container_tools/inspect_presentation_package_integrity.py"),
  layoutValidatorPath: path.join(skillDir, "container_tools/inspect_presentation_layout_geometry.py"),
  layoutArgs: ["--expected-slide-size-emu", "12192000,6858000", "--validate-heading-fit"],
  explicitTotalSlideCount: 44,
  requiredNativeTableOwnerSlides: [],
  fontPolicy: { basis: "design", families: ["DejaVu Sans"] },
  verifyArtifactToolImport: true,
  receiptPath: path.join(stagingDir, "ai-security-reference-architectures.validation-r11.json"),
});
console.log(JSON.stringify(result, null, 2));
