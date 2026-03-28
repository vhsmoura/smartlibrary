# SmartLibrary 📚
## Sistema de Gestão de Biblioteca Escolar - Projeto Integrador Univesp

### 🎯 **Objetivo do Projeto**
Desenvolver sistema web para **bibliotecas escolares** que reduz perdas/atrasos de livros em **50%**, controlando empréstimos com prazos de **80 dias**, notificações visuais e relatórios automáticos. Foco: **escolas públicas próximas ao polo Univesp** (SP).

**Problema resolvido:** Empréstimos sem registro → 20-30% livros "perdidos" por semestre.

### 🚀 **Funcionalidades**
- ✅ Cadastro livros com **fotos**
- ✅ Separação **Disponíveis** (verde) / **Emprestados** (vermelho)
- ✅ Contador **dias restantes** (80 dias prazo)
- ✅ Admin automático (`/admin`)
- ✅ **Responsivo** + acessível (WCAG)
- ✅ Logos **Univesp + SmartLibrary**

### 🛠 **Tecnologias**
| Frontend | Backend | Banco |
|----------|---------|-------|
| HTML5, CSS3 (paleta azul/verde acessível) | **Django 5.0** | **SQLite** |

### 📁 **Estrutura do Projeto**
```
PROJETO PI/
├── manage.py              # Executa servidor
├── livros/                # App principal
│   ├── models.py         # Livro (título, foto, aluno, datas)
│   ├── views.py          # Separa disponíveis/emprestados
│   └── admin.py          # Interface admin
├── templates/            # HTML
│   └── index.html        # Site completo
├── static/               # CSS + logos
└── media/                # Fotos livros
```

### 🔧 **Como Instalar e Usar**

#### **1. Pré-requisitos**
```bash
Python 3.9+ instalado
```

#### **2. Clone/Instale**
```bash
git clone [seu-repo]  # ou baixe ZIP
cd smartlibrary
pip install -r requirements.txt  # ou pip install django pillow
```

#### **3. Configure Banco**
```bash
python manage.py makemigrations livros
python manage.py migrate
python manage.py createsuperuser  # admin / MinhaSenha123!
```

#### **4. Cadastre Livros**
```
http://localhost:8000/admin/
→ Livros → ADD LIVRO
→ Título: "Harry Potter" | Autor: "JK Rowling" | Foto: upload
```

#### **5. Execute**
```bash
python manage.py runserver
```
**Acesse:** `http://localhost:8000`

### 📖 **Como Funciona o Código**

#### **Model `Livro`** (`livros/models.py`)
```python
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='livros/')
    aluno = models.CharField(max_length=100, blank=True)  # Vazio = disponível
    data_devolucao = models.DateField(null=True, blank=True)  # +80 dias
    
    def dias_restantes(self):  # Calcula prazo automaticamente
        return (self.data_devolucao - timezone.now().date()).days
```

#### **View Separação** (`livros/views.py`)
```python
def home(request):
    disponiveis = Livro.objects.filter(aluno__isnull=True)
    emprestados = Livro.objects.filter(aluno__isnull=False)
    # Template recebe listas separadas
```

#### **Template Dinâmico** (`templates/index.html`)
```html
{% for livro in livros_disponiveis %}
  <!-- Cards VERDES: Disponíveis -->
{% endfor %}

{% for livro in livros_emprestados %}
  <!-- Cards VERMELHAS: Emprestados + dias -->
{% endfor %}
```

### 🎨 **Design Acessível**
- **Paleta:** Azul (#47A3B2) / Verde (#026833) / Contraste AAA
- **Responsivo:** Mobile-first (grid auto-fit)
- **Header fixo** com logos clicáveis (Univesp externo)

### 📊 **Demonstração**
1. **Site:** localhost:8000 → Catálogo separado
2. **Admin:** localhost:8000/admin → CRUD livros
3. **Teste:** Emprestar livro → muda de verde→vermelho automaticamente


### 📈 **Impacto Esperado (PI Univesp)**
- **Redução 50%** atrasos/perdas livros
- **Relatórios** rotatividade acervo
- **Escalável** para múltiplas escolas


**Projeto Integrador Univesp 2026** | **SmartLibrary** - Transformando bibliotecas escolares! 🎓
