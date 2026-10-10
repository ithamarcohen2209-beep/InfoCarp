# Public synchronization audit — 10 October 2026

The full current application repository was inventoried against all public-site files, rather than comparing only the latest PR. The site intentionally remains a legal/support repository.

## Public-safe updates

Current feature/support descriptions, shopping estimate limits, external image-processing disclosure, account/data deletion instructions, source version facts and independent static-site setup, strict Python type checking, lint, tests and validation are synchronized. Public page links, styles and branding remain independent from the application UI.

## Intentional exclusions

- Application/backend/native implementation, assets, dependencies and implementation tests remain in the separately maintained private application repository under the existing publication boundary.
- Production configuration, credentials, tokens and signing identities are excluded to protect access and release security.
- Internal CI/CD, diagnostics, infrastructure configuration, schema/migration history and operational runbooks are excluded because this site does not implement or operate the application.
- Backup/recovery code, keys, storage details and status are excluded because they are private operational information.
- User/customer data, individual incident evidence and recovery reports are excluded to protect privacy.
- Private repository history is not imported. Public history remains separate.

These exclusions are deliberate, not an assertion that the public site contains the entire app. Publishing application source would require a separate explicit publication decision and security/licensing review.

## Remaining differences and limits

The public site is English and static; the app UI supports Hebrew, English and Russian and has native/backend dependencies. No application APIs, production environment examples, native builds or TypeScript configuration belong to this site. It requires no environment variables, so an `.env.example` is not applicable. Existing public historical commits may retain old operational prose; updating current files does not rewrite history.

Feature descriptions were reconciled with current implementation rather than copying stale private README/version prose. Runtime source availability, store prices, provider retention and app-store publication must not be inferred from this documentation audit. Site validation results are distinct from application/device or authenticated production tests.
