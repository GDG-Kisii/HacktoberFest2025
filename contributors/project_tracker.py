from email_notifier import EmailNotifier

class ProjectTracker:
    def __init__(self, enable_notifications=False):
        self.contributors = {}
        self.enable_notifications = enable_notifications
        self.notifier = EmailNotifier() if enable_notifications else None

    def add_contributor(self, name, username, email):
        self.contributors[username] = {
            "name": name,
            "email": email,
            "contributions": 0
        }
        if self.enable_notifications:
            token = self.notifier.generate_verification_token(email, username)
            subject = "🎉 Welcome to Hacktoberfest 2025!"
            body = f"Hello {name}! Verify your email using token: <b>{token}</b>"
            self.notifier.send_email(email, subject, body)
        return self.contributors[username]

    def add_contribution(self, username, repo, contribution_type, message):
        if username not in self.contributors:
            print(f"❌ Contributor '{username}' not found!")
            return
        self.contributors[username]['contributions'] += 1
        print(f"✅ Contribution added for {username}: {contribution_type} in {repo}")
