# 📚 Session 18 – Data, ML, DL & AI (Final Organized Notes)

---

## 🧠 أولًا: أنواع الأنظمة البيانية

### 🔹 OLTP vs OLAP

#### 1️⃣ OLTP (Online Transaction Processing)

📌 نظام مسؤول عن العمليات اليومية (Day-to-Day Operations)

* تسجيل Order
* إضافة / تعديل عميل
* حذف بيانات

✅ **الخصائص:**

* سرعة عالية جدًا ⚡️
* كل Query بتتعامل مع داتا قليلة
* Queries بسيطة (Insert – Update – Delete)
* Normalized Tables
* بيدعم Transactions (ACID)

📍 **مثال:**

* سوبر ماركت بيسجل كل عملية بيع
* حجز تذكرة
* تسجيل طالب في جامعة

📌 **جملة تحفظ:**

> OLTP بيخدم المستخدم

#### 2️⃣ OLAP (Online Analytical Processing)

📌 نظام مسؤول عن التحليل واتخاذ القرار

* تحليل المبيعات
* تقارير شهرية / سنوية
* مقارنة فروع أو سنوات

✅ **الخصائص:**

* داتا ضخمة 📊
* Queries معقدة
* قراءة أكتر من كتابة
* Denormalized Tables
* Star Schema / Snowflake Schema

📍 **مثال:**

تحليل مبيعات آخر 5 سنين لمعرفة:

* أفضل فرع
* أقل منتج مبيعًا

📌 **جملة تحفظ:**

> OLAP بيخدم الإدارة

---

## 🔍 الفرق بين Data Analysis و Data Science و AI

### 🟡 Data Analysis (DA)

📌 **هدفه:** فهم اللي حصل

* وصف الداتا
* Reports
* Dashboards
* Insights

🧰 **Tools:**

* SQL
* Excel
* Power BI
* Python

❓ **سؤال بيجاوب عليه:**

> إيه اللي حصل؟ وليه حصل؟

📍 **مثال:**

ليه المبيعات قلت الشهر اللي فات؟

### 🔵 Data Science (DS)

📌 **هدفه:** التنبؤ باللي هيحصل

* Models
* Machine Learning
* Predictions

🧰 **Tools:**

* Python
* ML
* Statistics

❓ **سؤال بيجاوب عليه:**

> إيه اللي ممكن يحصل قدام؟

📍 **مثال:**

هل المبيعات هتقل الشهر الجاي؟

### 🔴 Artificial Intelligence (AI)

📌 **هدفه:** اتخاذ القرار وتنفيذ Action

* Chatbots
* Face Recognition
* Self-driving Cars

⚠️ **الفرق المهم:**

> AI يقدر ياخد قرار
> DS بيقترح، لكن لا ينفذ

📍 **مثال:**

* DA: المبيعات قلت
* DS: يتوقع إنها هتقل تاني
* AI: يقلل السعر تلقائي

📌 **ملخص ذهبي:**

* DA → Support Decision
* DS → Suggest Decision
* AI → Take Decision

---

## 🧩 العلاقة بين AI – ML – DL

```
AI
 └── ML
      └── DL
```

📌 **جملة مهمة:**

> كل DL هو ML
> مش كل ML هو DL

### 🔹 الفرق بين ML و DL

| Machine Learning         | Deep Learning             |
| ------------------------ | ------------------------- |
| داتا أقل                 | داتا ضخمة جدًا            |
| Feature Engineering يدوي | Feature Extraction تلقائي |
| Models بسيطة             | Neural Networks           |
| أسرع                     | أبطأ                      |
| مناسب Structured Data    | ممتاز Unstructured Data   |

### 🧠 Feature Engineering vs Feature Extraction

#### 🔸 Feature Engineering

📌 الإنسان بيختار ويصنع الخصائص يدويًا

📍 **مثال:**

* السن
* الطول
* عدد المواد

➡️ مستخدم أكتر في ML

#### 🔸 Feature Extraction

📌 الموديل بيستخرج الخصائص من داتا خام

📍 **مثال:**

* Edges
* Shapes
* Patterns

➡️ مستخدم في DL

📌 **ملحوظة مهمة:**

> Feature Extraction جزء من Feature Engineering لكن FE أوسع

### 🐶🐱 مثال تطبيقي

**App يحدد قطة ولا كلب**

❓ نستخدم ML ولا DL؟

✅ **Deep Learning**

**ليه؟**

* الصور = Unstructured Data
* مستحيل نحدد Features يدويًا

📌 لو ML:

* شكل ودان؟
* لون؟
* حجم؟
  ❌ صعب جدًا

### 🧩 خطوات الحل (DL)

1️⃣ جمع صور قطط وكلاب
2️⃣ تنظيف الداتا
3️⃣ تقسيم Train / Test
4️⃣ استخدام CNN
5️⃣ Training
6️⃣ Prediction

📌 نظريًا:

> Pixels → Edges → Shapes → Object

### ❓ ليه ML داتا أقل و DL داتا أكبر؟

**ML:**

* Models بسيطة
* Features جاهزة
* لو الداتا كبرت → Overfitting

**DL:**

* بيتعلم من الصفر
* ملايين Parameters
* محتاج: داتا ضخمة 📦, وقت ⏳, GPU 💻

### 🔄 Epoch في Deep Learning

📌 **Epoch = لفة كاملة على الداتا**

📍 **مثال:**

1000 صورة → Epoch = الموديل يشوفهم كلهم مرة

⚠️ كل ما يزيد:

* التعلم يزيد
* خطر Overfitting يزيد

📌 **ملحوظة:**

> Epoch ≠ Iteration
> Iteration = Batch واحدة

### 🧠 ملحوظة ختامية مهمة

> التكرار مش عيب في ML، العيب إن الموديل يحفظ مش يفهم

---

# 📦 Session 18 – Part 2

## Data Types & Machine Learning Pipeline (Final Version)

### 🧠 أولًا: أنواع الداتا (Data Types)

📌 فهم نوع الداتا هو أول خطوة صح 👀 لأنه بيحدد:

* هتتخزن إزاي
* هتتعالج إزاي
* تستخدم ML ولا DL

### 📂 1️⃣ أنواع الداتا حسب الشكل (Structure)

#### 🟩 Structured Data

📌 داتا منظمة جدًا

* Rows & Columns
* Schema واضح
* كل Column ليه Data Type ثابت

📍 **بتتخزن في:**

* SQL Server
* MySQL
* PostgreSQL

📊 **مثال:**

| ID | Name  | Grade |
| -- | ----- | ----- |
| 1  | Ahmed | 85    |

✅ **مميزاتها:**

* سهلة التحليل
* Queries سريعة
* ممتازة للـ Data Analysis و ML

❌ **عيوبها:**

* مش مناسبة للصور، الفيديو، الصوت

📌 **استخدام شائع:**

* تقارير – Dashboards – ML Models

#### 🟥 Unstructured Data

📌 داتا غير منظمة

* مفيش Rows & Columns
* شكلها حر

📍 **أمثلة:**

* صور 🖼️
* فيديو 🎥
* صوت 🎧
* Text (Posts, Reviews)

📍 **بتتخزن غالبًا في:**

* File Systems
* Object Storage
* ومعاها Metadata في NoSQL

❌ صعب تحليلها مباشرة ✅ ممتازة للـ Deep Learning

📌 **مثال:**

* صورة قطة → الموديل يستخرج الخصائص لوحده

#### 🟨 Semi-Structured Data

📌 داتا في النص، مش Tables لكن ليها تنظيم جزئي

📍 **أمثلة:**

* JSON
* XML
* Logs

```json
{
  "name": "Ahmed",
  "age": 22,
  "city": "Cairo"
}
```

📍 **بتتخزن في:**

* MongoDB
* Firebase

✅ مرنة ❌ مش منظمة زي SQL

📌 **جملة مهمة:**

> Semi-Structured Data لها Schema بس Schema مرن ومش ثابت

### 🧩 مقارنة سريعة

| النوع           | التخزين       | الاستخدام |
| --------------- | ------------- | --------- |
| Structured      | SQL           | DA / ML   |
| Semi-Structured | NoSQL         | ML / APIs |
| Unstructured    | Files / NoSQL | DL        |

### 🔢 2️⃣ أنواع الداتا حسب القيم (Values)

#### 🔵 Continuous Data

📌 قيم رقمية متصلة، تقبل الكسور، ليها مدى

📍 **أمثلة:**

* درجة: 78.5
* طول: 170.2
* سعر: 1050.75

📌 **بتستخدم في:** Regression, Statistics

#### 🟠 Categorical Data

📌 قيم تصنيفية، Labels / Classes

📍 **أمثلة:**

* Gender: Male / Female
* Result: Pass / Fail

📌 **بتستخدم في:** Classification

#### 🟣 Ordinal Data (إضافة مهمة)

📌 نوع خاص من Categorical، ليه ترتيب لكن مش رقمية

📍 **مثال:**

* Poor – Good – Excellent
* Grades: ضعيف – جيد – ممتاز

📌 مهمة لأنها:

* Categorical لكن بترتيب
* 🔄 تحويل Continuous → Categorical

📍 **مثال درجات الطلاب:**

| الدرجة | التقدير  |
| ------ | -------- |
| 95     | ممتاز    |
| 82     | جيد جدًا |
| 68     | جيد      |
| 45     | ضعيف     |

📌 ليه نعمل كده؟

* تبسيط القرار
* مناسب لمشاكل Classification

📌 الاسم العلمي: Discretization / Binning

---

## ⚙️ ثانيًا: Machine Learning Pipeline (شرح تفصيلي بمثال واحد ثابت)

### 🎓 مثالنا: توقع نجاح الطالب (Pass / Fail)

1️⃣ **Data Collection**

📌 جمع الداتا من مصادر مختلفة

📍 **مصادر:**

* Excel
* SQL
* Google Forms

📊 **مثال Features:**

* درجات
* نسبة حضور
* عدد ساعات مذاكرة

2️⃣ **Data Preprocessing ⚠️**

📌 أهم مرحلة في الـ Pipeline

* Handling Missing Values
* Encoding للـ Categorical
* Scaling للأرقام

📍 **مثال:**

* Male / Female → 0 / 1
* ملء القيم الناقصة بالـ Average

3️⃣ **Feature Selection / Engineering**

📌 اختيار أو إنشاء أهم الخصائص

📍 **مثال:**

* ساعات المذاكرة ✔️
* لون القميص ❌

📌 **الهدف:**

* تقليل الضوضاء
* تحسين أداء الموديل

4️⃣ **Train / Test Split**

📌 تقسيم الداتا:

* 70% Training
* 30% Testing

📌 **السبب:**

* نعرف هل الموديل فهم ولا حفظ الداتا

5️⃣ **Modeling**

📌 اختيار الخوارزمية المناسبة

📍 **أمثلة:**

* Logistic Regression
* Decision Tree

📌 **الاختيار يعتمد على:**

* نوع الداتا
* نوع المشكلة

6️⃣ **Training**

📌 تعليم الموديل باستخدام Train Data

📍 **مثال:**

* طالب بيذاكر أكتر → فرص نجاح أعلى

7️⃣ **Testing**

📌 اختبار الموديل على داتا جديدة (الموديل مش شافها قبل كده)

📌 **الهدف:** اختبار التعميم (Generalization)

8️⃣ **Evaluation**

📌 تقييم الأداء بالأرقام

📊 **Metrics:**

* Accuracy
* Precision
* Recall

📍 **مثال:**

* Accuracy = 85%

📌 **فرق مهم:**

* Testing → تشغيل
* Evaluation → قياس

9️⃣ **Tuning**

📌 تحسين الموديل عن طريق:

* تغيير Hyperparameters
* تجربة Models مختلفة

📍 **مثال:**

* Depth في Decision Tree
* Learning Rate

🔟 **Prediction**

📌 استخدام الموديل فعليًا

📍 **مثال:**

* طالب جديد → ناجح / راسب

1️⃣1️⃣ **Monitoring**

📌 متابعة الموديل بعد التشغيل

* الداتا بتتغير
* الأداء ممكن يقل

📍 **مثال:**

* مستوى الطلاب السنة دي أقل → نحتاج Retraining 

🚀 **Production (إضافة مهمة)**

📌 نشر الموديل داخل:

* App
* Website
* System

📌 **السبب:**

* User حقيقي يستخدمه

### 🧠 ملاحظة ختامية

> التكرار مش عيب في ML، العيب إن الموديل يحفظ مش يفهم
