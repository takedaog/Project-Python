#  EduPlatform — Ta'lim Platformasi (OOP, Python)

Bu loyiha Python’da yaratilgan, `Kundalik.com`’ga o‘xshash backend’siz ta'lim platformasidir. Ma'lumotlar vaqtincha xotirada (in-memory) saqlanadi, OOP asosida sinflar orqali boshqariladi.

---

## Texnologiyalar

- Python 3.x
- Object-Oriented Programming (OOP)
- openpyxl (Excel eksporti uchun)
- csv (CSV eksporti uchun)
- Standart Python `file` operatsiyalari (SQL eksport uchun)

---

##  Loyihaning Strukturasi

```plaintext
eduplatform/
│
│
├── models/                        # Barcha foydalanuvchi rollari va asosiy obyektlar
│   ├── abstract_role.py           # AbstractRole — barcha rollarning bazasi
│   ├── user.py                    # User — asosiy foydalanuvchi
│   ├── student.py                 # Student — baho ko‘rish, topshiriq topshirish
│   ├── teacher.py                 # Teacher — vazifa berish, baho qo‘yish
│   ├── parent.py                  # Parent — farzandni kuzatish
│   ├── admin.py                   # Admin — foydalanuvchilarni boshqarish
│   ├── assignment.py              # Assignment — vazifalar
│   ├── grade.py                   # Grade — baholar
│   ├── schedule.py                # Schedule — dars jadvallari
│   ├── notification.py            # Notification — xabarnomalar
│
├── data/
│   └── database.py                # In-memory "bazasi": users, assignments, grades, va h.k.
│
├── export/                        # Eksport funksiyalari
│   └── exporter.py                # .xlsx, .csv, .sql formatlarga eksport
│
├── scraped_data/                  # OLX saytidan olingan tozalangan ma'lumotlar
│   └── olx_cleaned.csv
│
│
├──tests/                          # Testlar
│   ├── test_exporter.py        
│   ├── test_user.py           
│   ├── test_student.py   
│   ├── test_teacher.py              
│   ├── test_parent.py               
│   ├── test_admin.py                   
│   ├── test_assignment.py              
│   ├── test_grade.py                   
│   ├── test_schedule.py                
│   ├── test_notification.py 
|   ├── test_database.py
|
└── README.md                      # Loyihaning tushuntiruvchi hujjat