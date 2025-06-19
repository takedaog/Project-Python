from models.user import User

user = User(1, "Ali Valiyev", "ali@example.com", "hashedpassword123", "Student")
user.add_notification("Yangi vazifa yuklandi.")
user.add_notification("Bahoyingiz 5!")

for note in user.view_notifications():
    print(f"[{note['created_at']}] {note['message']}")

user.delete_notification(1)

print("Qolgan xabarlar:")
print(user.view_notifications())