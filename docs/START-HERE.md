# Start here

You do not need to know what a repository is. It is simply a versioned folder of shared materials.

## 1. Get your own folder

[Download the release ZIP](https://github.com/Dima8894/agent-workshop-starter-kit/releases/latest/download/agent-workshop-starter-kit.zip). Extract it before opening it. Put it somewhere you can find again, such as `Documents/My AI Workshop`. Keep a backup of your personal work.

## 2. Choose one assistant

**Codex with local files:** follow the [official setup guide](https://learn.chatgpt.com/docs/quickstart), sign in, and select the extracted folder for the task. Interface labels and account access can change. This kit does not require an API key or a specific paid tier.

**Another local assistant:** open the same folder and explicitly ask it to read AGENTS.md. CLAUDE.md is included as a compatibility entry point; tool-specific behavior should be checked in your installed app.

**A chat without local files:** paste CHATGPT-START.txt into a new chat. Attach only the fictional example or permitted material. Save the named documents it returns yourself. Read [chat mode](CHATGPT.md).

Local files can still be sent to the AI provider for processing. Start with the fictional example if you are unsure about data permission.

## 3. Send FIRST-PROMPT.txt

Copy its text into the chat. The assistant asks one question at a time. You can say “show me an example,” “skip,” or “pause.” You do not have to complete every template before seeing a result.

If you attended Agent Workshop, add a readable photo of your worksheet or type its key points. If not, describe one task in ordinary words.

## 4. Check the result

Ask the assistant to point to the input behind each conclusion. Verify at least one calculation or statement yourself. Try removing a necessary value. A good assistant flags the gap rather than inventing an answer.

## 5. Continue tomorrow

Keep your workspace folder. In a new session opened on the same kit, send:

> Read AGENTS.md and workspace/START.md. Resume my current project from the latest checks. Preserve existing work.

Without file access, attach your saved task, workflow, checks, onboarding state, and progress instead.

## If something goes wrong

| Problem | Next action |
| --- | --- |
| The assistant cannot see files | Select the extracted folder or use chat mode; do not assume it saved anything. |
| It asks a long questionnaire | Say “One question at a time; use the answers I already gave you.” |
| It starts writing code immediately | Say “Start with a document or table unless code is necessary.” |
| It wants private data | Switch to fictional data with the same structure. |
| A result is wrong | Record the error in checks.md, correct the rule, and rerun that case. |
| A file already exists | Resume from it; never replace it with a blank template. |
| Access or subscription is unavailable | Use an approved alternative; account access is separate from this free kit. |

The [official AGENTS.md guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md) explains instruction discovery. Other folder conventions in this kit are our design, not requirements imposed by OpenAI. Documentation reviewed on 2026-10-25.
