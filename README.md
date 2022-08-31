# ECM251-2022
Repositório da disciplina de ECM251

# ECM251 - Utilizando Git

Em primeiro lugar, configurar quem é o usuário (***nome***) e qual seu ***e-mail***.

```bash
git config --global user.name "nomeusuario"
git config --global user.email email@email.com
```

Ordem para criar um repositório:
- Inicializao o reposítório
```bash
git init
```

- Adicionar os arquivos com:
```bash
git add .
```

- Comitar (salvar) os arquivos:
```bash
git commit -m "mensagem"
```

- Verificar o status:
```bash
git status
```

- Listar os arquivos no diretorio:
```bash
ls -l
```

- Criar e mudar para uma nova branch
```bash
git checkout -b <nomeDaBranch>
```

- Mudar pra branch já existente
```bash
git checkout <nomeDaBranch>
```
