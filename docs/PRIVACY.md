# Keep your work private

The public repository contains blank templates and fictional examples. Your answers, business rules, inputs, and outputs belong under workspace/, which is excluded from normal Git tracking and from the release file allowlist.

**Local storage does not mean offline AI processing.** Follow your organization's rules for the assistant you use. Start with fictional examples; remove personal and confidential details before attaching documents.

Do not paste credentials into chats or templates. Use the application's approved authentication flow if you later connect a tool. Do not include customer lists, employee files, meeting recordings, or internal financial data in public issues.

Gitignore is a convenience, not access control. It does not hide already tracked files, prevent forced adds, block connectors, or protect files in a manually zipped folder. Before sharing, make a clean copy from the release and add only reviewed, sanitized examples. Never publish your whole workspace folder.

The included package builder uses an explicit allowlist and rejects symlinked paths. It does not include workspace even if that folder exists. The validator checks common accidental disclosures, but it is not a complete secret scanner. Review the exact staged diff and file list before publication.

The kit contains no analytics, external scripts, account registration, or telemetry. AI providers and any integrations you choose operate under their own policies.

If a secret is published, revoke it at its provider, stop further distribution, and follow the hosting platform's guidance for removing sensitive history. Deleting the latest file alone does not remove earlier copies.
