# STI Information Assistant v2

Enhanced academic/research prototype with:
- SQLite/SQLAlchemy database
- authenticated admin content management
- expert-review/approval workflow
- English/Kiswahili seeded content
- trained TF-IDF + Logistic Regression intent classifier
- held-out evaluation artifacts
- audit logging
- consent-gated inquiry storage
- pseudonymous sessions and basic identifier redaction
- configurable retention cleanup

## Run
`pip install -r requirements.txt`

Set `ADMIN_USERNAME` and a strong `ADMIN_PASSWORD`, then run `streamlit run app.py`.

## Train/evaluate
`python train_model.py`

The included dataset is only a demonstration corpus. Do not claim its metrics as production or thesis-grade performance. Replace it with a substantially larger human-annotated Kenyan English/Kiswahili corpus and a locked held-out test set.

## Content governance
Seeded content is `pending_review`. Only explicitly approved content is shown to users. The application does not manufacture expert approval. A qualified Kenyan STI clinician/public-health reviewer and Kiswahili health-communication reviewer should approve the content before deployment.

## Clinical safety
Educational only. The system does not diagnose or prescribe. Symptoms do not confirm gonorrhoea.

## Privacy
No direct identifiers should be entered. Storage is opt-in; stored inquiries use a pseudonymous session hash; raw inquiry text is excluded from audit events; administrators can run retention deletion.

For real deployment add HTTPS/TLS, encrypted database/backups, managed secrets, least-privilege access, rate limiting, hardened sessions, monitoring, a formal privacy/data-protection review and an incident-response process.
