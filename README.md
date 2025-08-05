# Teste Técnico – Desenvolvedor Full Stack

## Descrição  
Aplicação Django para gerenciar vagas e candidatos, com dashboard de estatísticas usando Pandas e Chart.js.

## Tecnologias  
- Python 3.13.1
- Django 5.2.4
- Pandas  
- Chart.js  
- Bootstrap 5  

## Instalação  
```bash
git clone https://github.com/SeuUsuario/Vagas_teste.git
cd Vagas_teste
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Uso
Admin: http://127.0.0.1:8000/admin/
Dashboard: http://127.0.0.1:8000/dashboard/

Estrutura
Vagas_teste/
├── core/           # app com models, views, admin, urls, templates
├── vaga_bauer/     # pacote do projeto (settings, urls, wsgi, etc.)
├── manage.py
├── requirements.txt
└── .gitignore
