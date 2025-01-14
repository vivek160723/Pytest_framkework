import pytest

class TestEmailPassword:
    @pytest.mark.parametrize("email,password", [
        ("test@example.com", "password123"),
        ("admin@example.com", "adminpass"),
        ("user@example.com", "user123"),
        ("guest@example.com", "guest123")
    ])
    def test_email_password(self, email, password):
        # Example validation: Check if the password matches a specific pattern
        valid_emails = ["test@example.com", "admin@example.com", "user@example.com", "guest@example.com"]
        valid_passwords = ["password123", "adminpass", "user123", "guest123"]

        assert email in valid_emails, f"Invalid email: {email}"
        assert password in valid_passwords, f"Invalid password for email {email}"