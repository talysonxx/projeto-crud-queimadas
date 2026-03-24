# 🔥 Monitoramento de Queimadas (Projeto Acadêmico)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092e20.svg?style=for-the-badge&logo=django&logoColor=white)
![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-%237EBC6F.svg?style=for-the-badge&logo=openstreetmap&logoColor=white)

Este projeto foi desenvolvido como um trabalho bimestral universitário. O sistema fornece uma plataforma centralizada para o registro e visualização de focos de incêndio, integrando dados geoespaciais com controle de acesso rigoroso para garantir a confiabilidade das informações.

## 📋 Sobre o Projeto

O sistema permite que qualquer pessoa visualize em tempo real a localização e a intensidade das queimadas. No entanto, para manter a integridade dos dados, apenas profissionais devidamente identificados podem realizar novos registros.

### Principais Funcionalidades:
* **Painel de Ocorrências:** Listagem intuitiva com o nome do local, coordenadas e nível de intensidade.
* **Mapa Interativo (OpenStreetMap):** Ao selecionar uma ocorrência na lista, o mapa renderiza automaticamente o ponto exato do foco de incêndio.
* **Controle de Acesso:** Área restrita para bombeiros. Apenas usuários cadastrados e que possuam credencial **CLB** (Bombeiro) podem adicionar novas ocorrências.

---

## 🛠️ Tecnologias e Arquitetura

O projeto utiliza uma stack moderna para garantir performance e facilidade de manutenção:
* **Linguagem:** Python 3.x
* **Framework Web:** Django (MTV Architecture)
* **Frontend:** HTML5, CSS3 (Design responsivo)
* **Mapas:** API OpenStreetMap (via Leaflet.js ou similar)
* **Banco de Dados:** SQLite (padrão de desenvolvimento)

### Colaboração do Grupo:
Este projeto foi o resultado de um esforço conjunto, com a seguinte divisão de responsabilidades:
* **Backend & Integração de APIs:** [Seu Nome Aqui]
* **Modelagem de Dados & Banco de Dados:** [Nome do Colega]
* **Interface (Templates & UI/UX):** [Nome do Colega]

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar o ambiente em sua máquina local:

### 1. Clonar o repositório
```bash
git clone [https://github.com/seu-usuario/projeto-queimadas-naldo.git](https://github.com/seu-usuario/projeto-queimadas-naldo.git)
cd projeto-queimadas-naldo
