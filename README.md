# BioForgePipeline
BioForge Pipeline Mini Project
BioForge

خط لوله جامع تحلیل داده‌های ژنتیکی

BioForge یک پروژه پایتونی برای طراحی و پیاده‌سازی یک Pipeline خط فرمانی (CLI) جهت پردازش و تحلیل توالی‌های DNA است.

هدف پروژه، تمرین طراحی نرم‌افزار تمیز، قابل فهم و قابل دفاع در مقیاس کوچک و استفاده صحیح از مفاهیم برنامه‌نویسی شیءگرا (OOP) است.

Pipeline پروژه مراحل مختلفی را از دریافت فایل FASTA تا تولید گزارش نهایی و ثبت خطاها و Warningها انجام می‌دهد.

---

Pipeline پروژه

جریان کلی پردازش در BioForge به صورت زیر است:

FASTA Input
    ↓
Parsing
    ↓
Validation
    ↓
ORF Detection
    ↓
Translation
    ↓
Filtering
    ↓
Annotation
    ↓
Reporting
    ↓
Logging

---

ویژگی‌های پروژه

پروژه قابلیت‌های زیر را پوشش می‌دهد:

- خواندن فایل FASTA چندرکوردی
- استخراج ID و Description از Header
- اعتبارسنجی توالی DNA
- تشخیص توالی‌های نامعتبر
- محاسبه Complement
- محاسبه Reverse Complement
- تبدیل DNA به RNA
- محاسبه GC Content
- تشخیص ORF در Reading Frameهای مختلف
- بررسی Strandهای Forward و Reverse
- تشخیص ORFهای Complete و Incomplete
- ترجمه Codonها به Amino Acid
- محاسبه وزن مولکولی Protein
- فیلتر کردن Proteinها
- اختصاص ID به ORFهای نهایی
- تولید Report
- ثبت خطاها و Warningها در فایل Log

---

ساختار پروژه

ساختار کلی پروژه به صورت زیر است:

BioForgePipeline/
│
├── data/
│   ├── codon_table.txt
│   └── amino_weights.txt
│
├── input/
│   └── input.fasta
│
├── output/
│   ├── report.txt
│   └── bioforge.log
│
├── src/
│   │
│   ├── fasta/
│   │   ├── dna_ops.py
│   │   ├── parser.py
│   │   ├── record.py
│   │   └── validator.py
│   │
│   ├── orf/
│   │   ├── forward.py
│   │   ├── orf.py
│   │   └── reverse.py
│   │
│   ├── translation/
│   │   ├── data_loader.py
│   │   ├── protein.py
│   │   └── translation.py
│   │
│   ├── filtering/
│   │   ├── filtering.py
│   │   └── length_filter.py
│   │
│   └── reporting/
│       ├── annotator.py
│       ├── pipeline.py
│       └── reporter.py
│
└── main.py



---

ورودی پروژه

ورودی اصلی برنامه یک فایل FASTA چندرکوردی است.

نمونه:

>seq001 organism=E_coli sample=A
ATGCTTTCATAG

>seq002 organism=Human sample=B
CCCATGGGGTAA

هر Record شامل سه بخش اصلی است:

- "ID"
- "Description"
- "Sequence"

در Header، اولین بخش به عنوان ID در نظر گرفته می‌شود و اطلاعات بعدی به عنوان Description پردازش می‌شوند.

در صورت وجود "organism=..."، مقدار مربوط به organism نیز باید قابل استخراج باشد.

---

FASTA Parsing

بخش Parsing مسئول خواندن و پردازش فایل FASTA است.

ویژگی‌های مورد انتظار:

- پشتیبانی از چند Record
- نادیده گرفتن خطوط خالی
- پذیرش حروف کوچک
- تشخیص فایل خالی
- تشخیص وجود Sequence قبل از اولین Header
- تشخیص Header بدون Sequence
- ثبت IDهای تکراری به صورت Warning در Log

---

DNA Validation

توالی DNA در این پروژه از چهار Nucleotide تشکیل می‌شود:

A → Adenine
T → Thymine
C → Cytosine
G → Guanine

بنابراین یک DNA Sequence معتبر فقط باید شامل حروف "A"، "T"، "C" و "G" باشد.

در صورت نامعتبر بودن Sequence، خطای اختصاصی "InvalidSequenceError" ایجاد می‌شود.

توالی نامعتبر به صورت خودکار اصلاح، حذف یا جایگزین نمی‌شود.

---

DNA Operations

پروژه عملیات مختلفی را روی DNA Sequence انجام می‌دهد.

Complement

قواعد مکمل بودن:

A ↔ T
C ↔ G

مثال:

DNA:
ATGC

Complement:
TACG

---

Reverse Complement

Reverse Complement از دو مرحله تشکیل می‌شود:

1. ساخت Complement
2. Reverse کردن نتیجه

مثال:

DNA:
ATGC

Complement:
TACG

Reverse Complement:
GCAT

---

DNA → RNA

در تبدیل DNA به RNA، "T" به "U" تبدیل می‌شود:

A → A
T → U
C → C
G → G

مثال:

DNA:
ATGC

RNA:
AUGC

---

GC Content

GC Content درصد Nucleotideهای "G" و "C" در یک DNA Sequence است.

فرمول:

GC Content =
(Number of G + Number of C) / Total Length × 100

مثال:

DNA = ATGC

G = 1
C = 1
Length = 4

GC Content = 50%

---

ORF Detection

ORF مخفف Open Reading Frame است.

یک ORF از Codon شروع "AUG" آغاز می‌شود و در حالت کامل با یکی از Codonهای Stop به پایان می‌رسد:

UAA
UAG
UGA

Codonها باید سه‌تایی و در همان Reading Frame بررسی شوند.

مثال:

AUG | GCU | AAA | UGA

در این مثال:

Start Codon = AUG
Stop Codon  = UGA

بنابراین ORF کامل است.

---

Reading Frames

برای هر Sequence سه Reading Frame در جهت Forward و سه Reading Frame در جهت Reverse بررسی می‌شوند:

Forward Frame 0
Forward Frame 1
Forward Frame 2

Reverse Frame 0
Reverse Frame 1
Reverse Frame 2

در مجموع شش Reading Frame بررسی می‌شود.

در تشخیص ORF، Alignment مربوط به Codonها باید حفظ شود و صرفاً پیدا کردن اولین "AUG" و اولین Stop Codon کافی نیست.

---

Incomplete ORF

ممکن است یک "AUG" پیدا شود اما در همان Reading Frame هیچ Stop Codon معتبری وجود نداشته باشد.

در این حالت ORF حذف نمی‌شود و به عنوان ORF ناقص نگهداری می‌شود:

is_complete = False

در صورت پیدا شدن Stop Codon مناسب:

is_complete = True

بنابراین خروجی می‌تواند شامل هر دو نوع ORF باشد:

- Complete ORF
- Incomplete ORF

---

Reverse Strand

برای بررسی Reverse Strand، ابتدا Reverse Complement ساخته می‌شود و سپس سه Reading Frame مربوط به Reverse بررسی می‌شوند.

مختصات ORFهایی که از Reverse Strand پیدا می‌شوند باید در نهایت نسبت به DNA اصلی گزارش شوند.

اطلاعات مربوط به هر ORF شامل مواردی مانند موارد زیر است:

Strand
Frame
Start Position
Protein
Complete / Incomplete

---

Translation

Translation مرحله‌ای است که RNA را به Protein تبدیل می‌کند.

هر Codon شامل سه Nucleotide از RNA است و بر اساس جدول Codon به یک Amino Acid تبدیل می‌شود.

مثال:

AUG → M
CUU → L
UCA → S

بنابراین:

AUG CUU UCA

به:

MLS

ترجمه می‌شود.

---

Start Codon

Codon:

AUG

به عنوان Start Codon شناخته می‌شود و در این پروژه ORFها از "AUG" شروع می‌شوند.

---

Stop Codon

Stop Codonها عبارت‌اند از:

UAA
UAG
UGA

Stop Codonها نباید به عنوان Amino Acid در Protein نهایی قرار بگیرند.

مثال:

AUG CUU UCA UAG

نتیجه:

MLS

و "UAG" در Protein قرار نمی‌گیرد.

---

Data Files

برای Translation و محاسبه وزن مولکولی Protein، اطلاعات مورد نیاز در فایل‌های Data نگهداری می‌شوند.

data/
├── codon_table.txt
└── amino_weights.txt

codon_table.txt

این فایل شامل Codonها و Amino Acid متناظر با آنها است.

نمونه:

AUG M
UUU F
UAA *

اطلاعات این فایل نباید مستقیماً داخل کد Hardcode شوند.

---

amino_weights.txt

این فایل شامل کد یک‌حرفی Amino Acidها و وزن مولکولی آنها است.

نمونه:

A 71.037
C 103.009
M 131.040

اطلاعات وزن Amino Acidها نیز باید از فایل Data خوانده شوند.

در صورت خراب بودن یک خط از فایل‌های Data، خطا ایجاد شده و شماره خط مشکل‌دار باید مشخص شود.

---

Protein

Protein نتیجه Translation یک ORF است و Sequence مربوط به Amino Acidها را نگهداری می‌کند.

وزن مولکولی Protein نیز بر اساس Amino Acidهای تشکیل‌دهنده آن و اطلاعات موجود در "amino_weights.txt" قابل محاسبه است.

---

Filtering

پس از Translation، امکان فیلتر کردن Proteinها وجود دارد.

سه نوع Filter در مشخصات پروژه تعریف شده است:

Length Filter

Proteinها بر اساس طول Sequence فیلتر می‌شوند.

برای مثال:

--min-length 4

یعنی فقط Proteinهایی که حداقل چهار Amino Acid دارند انتخاب شوند.

---

Weight Filter

این Filter بر اساس وزن مولکولی Protein عمل می‌کند.

وزن Protein از وزن Amino Acidهای تشکیل‌دهنده آن محاسبه می‌شود.

---

Motif Filter

Motif یک الگوی مشخص از Amino Acidها در Protein است.

برای استفاده از Motif Filter، علاوه بر خود Motif، موقعیت آن در Protein نیز باید در دسترس باشد.

برای مثال:

Motif: TAG
Position: 4

پیدا کردن Motif و Filtering بر اساس آن دو مرحله جدا از یکدیگر هستند.

---

Annotation

پس از پردازش و Filtering، برای ORFهای نهایی ID خودکار ایجاد می‌شود.

نمونه:

BFG_001
BFG_002
BFG_003
...

---

Reporting

گزارش نهایی پروژه در فایل زیر تولید می‌شود:

output/report.txt

گزارش باید حداقل اطلاعات زیر را برای ORFها داشته باشد:

ID
Strand
Frame
Start Position
Protein
Complete / Incomplete

---

Logging

Log پروژه در مسیر زیر ذخیره می‌شود:

output/bioforge.log

مواردی که باید در Log ثبت شوند شامل:

- Record خراب
- Sequence نامعتبر
- ID تکراری
- Warningها
- خطاهای Data File

Log باید به صورت Append نوشته شود و اطلاعات قبلی را Overwrite نکند.

---

Exception Handling

ساختار Exceptionهای پروژه به صورت زیر تعریف شده است:

BioForgeError
├── FastaFormatError
├── InvalidSequenceError
└── DataFileError

BioForgeError

Exception پایه پروژه است.

FastaFormatError

برای خطاهای مربوط به ساختار فایل FASTA استفاده می‌شود.

InvalidSequenceError

برای DNA Sequenceهای نامعتبر استفاده می‌شود.

DataFileError

برای خطاهای مربوط به فایل‌های Data مانند "codon_table.txt" و "amino_weights.txt" استفاده می‌شود.

در صورت خراب بودن یک Record، در صورت امکان نباید کل Pipeline متوقف شود؛ Record خراب باید Log شود و پردازش Recordهای سالم ادامه پیدا کند.

---

Object-Oriented Design

این پروژه یک تمرین OOP است، اما هدف آن تبدیل کردن همه قسمت‌های پروژه به Class نیست.

در طراحی پروژه از مفاهیم اصلی OOP مانند موارد زیر استفاده می‌شود:

- Encapsulation
- Inheritance
- Polymorphism
- Composition

انتخاب Class یا Function باید بر اساس مسئولیت هر بخش انجام شود.

برای مثال، بخشی که فقط یک عملیات مستقل و بدون State انجام می‌دهد می‌تواند به صورت Function پیاده‌سازی شود، در حالی که بخشی که داده و رفتار مرتبط را در کنار هم نگهداری می‌کند می‌تواند به صورت Class طراحی شود.

---

Design Decisions

1. جداسازی Pipeline به بخش‌های مستقل

هر مرحله از Pipeline مسئولیت مشخصی دارد.

این جداسازی باعث می‌شود تغییر یا تست یک بخش، کمترین وابستگی را به بخش‌های دیگر داشته باشد.

---

2. جدا کردن Data از منطق برنامه

اطلاعات Codon و وزن Amino Acidها داخل فایل‌های Data نگهداری می‌شوند و مستقیماً داخل کد Hardcode نمی‌شوند.

این کار باعث می‌شود تغییر اطلاعات Data بدون تغییر منطق اصلی برنامه امکان‌پذیر باشد.

---

3. استفاده از Exceptionهای اختصاصی

به جای استفاده از Exceptionهای عمومی برای تمام خطاها، خطاهای اصلی پروژه در قالب Exceptionهای اختصاصی مدیریت می‌شوند.

این کار باعث می‌شود نوع خطا مشخص‌تر باشد و مدیریت آن در بخش‌های مختلف Pipeline ساده‌تر شود.

---

4. نگهداری ORFهای Complete و Incomplete

ORF ناقص حذف نمی‌شود و وضعیت آن با "is_complete" مشخص می‌شود.

به این ترتیب اطلاعات ORFهای ناقص نیز در Pipeline حفظ می‌شود.

---

5. جدا کردن Translation از Data Loading

خواندن جدول Codon و وزن Amino Acid از فایل Data از منطق Translation جدا شده است.

این جداسازی باعث می‌شود مسئولیت خواندن داده و مسئولیت تبدیل Codon به Protein از یکدیگر مستقل باشند.

---

6. جداسازی Filtering از تشخیص Motif

تشخیص Motif و Filtering بر اساس Motif دو وظیفه متفاوت هستند.

ابتدا اطلاعات مربوط به Motif و موقعیت آن ایجاد می‌شود و سپس Filter می‌تواند از این اطلاعات استفاده کند.

---

Command Line Interface

برنامه با استفاده از "argparse" از طریق Command Line اجرا می‌شود.

نمونه اجرای برنامه:

python main.py --input input/input.fasta --out output/ --min-length 4

پارامترهای اصلی:

Parameter| توضیح
"--input"| مسیر فایل FASTA ورودی
"--out"| مسیر ذخیره فایل‌های خروجی
"--min-length"| حداقل طول Protein برای Filtering

پارامتر "--min-length" باید واقعاً روی نتیجه Filtering تأثیر بگذارد.

---

File Handling

برای باز کردن فایل‌ها از Encoding مناسب استفاده می‌شود.

نمونه:

with open(..., encoding="utf-8")

مواردی مانند زیر باید مدیریت شوند:

- FileNotFoundError
- فایل خالی
- فایل خراب
- Data File نامعتبر
- FASTA نامعتبر

---

نمونه اجرای Pipeline

برای اجرای پروژه:

python main.py --input input/input.fasta --out output/ --min-length 4

Pipeline مراحل زیر را انجام می‌دهد:

FASTA
 ↓
Parsing
 ↓
Validation
 ↓
ORF Detection
 ↓
Translation
 ↓
Filtering
 ↓
Annotation
 ↓
Reporting
 ↓
Logging

در پایان، گزارش و Log در مسیر خروجی ایجاد می‌شوند:

output/
├── report.txt
└── bioforge.log

---

خروجی مورد انتظار

گزارش نهایی باید اطلاعات مربوط به ORFهای پردازش‌شده را شامل شود، از جمله:

ID
Strand
Frame
Start Position
Protein
Complete / Incomplete

همچنین خطاها و Warningهای مربوط به پردازش در فایل:

bioforge.log

ثبت می‌شوند.

---

هدف نهایی پروژه

با اجرای موفق Pipeline، برنامه باید بتواند:

1. فایل FASTA را بخواند.
2. Sequenceها را Parse کند.
3. Sequenceها را Validate کند.
4. ORFها را در هر ۶ Reading Frame پیدا کند.
5. Forward و Reverse Strand را بررسی کند.
6. ORFهای Complete و Incomplete را تشخیص دهد.
7. ORFها را Translate کند.
8. Proteinها را Filter کند.
9. ORFها را Annotate کند.
10. Report تولید کند.
11. خطاها و Warningها را در Log ثبت کند.

---

تکنولوژی‌های استفاده‌شده

- Python
- Object-Oriented Programming (OOP)
- argparse
- File Handling
- Exception Handling
- Logging
- FASTA Processing

---

نتیجه

BioForge یک Pipeline کوچک و ماژولار برای پردازش توالی‌های ژنتیکی است که مراحل مختلف پردازش DNA، تشخیص ORF، Translation، Filtering، Annotation و Reporting را در یک جریان مشخص به هم متصل می‌کند.

هدف اصلی پروژه علاوه بر پیاده‌سازی قابلیت‌های پردازش ژنتیکی، تمرین طراحی نرم‌افزار تمیز، مدیریت خطا، کار با فایل‌ها، استفاده مناسب از OOP و ایجاد یک برنامه قابل اجرا از طریق Command Line است.
