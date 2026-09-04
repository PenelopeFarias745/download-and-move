# Download & Move

Projeto desenvolvido em Python, consistindo de um organizador automático de arquivo. O programa monitora continuamente a pasta de Downloads e, sempre que um novo arquivo é baixado, identifica sua extensão e o move automaticamente para uma pasta correspondente ao seu tipo. Caso a pasta de destino ainda não exista, ela é criada automaticamente. Além disso, caso haja algum arquivo com o mesmo nome, ele gera um novo nome para evitar a substituição do arquivo existente.

---
## 📚 Aprendizados
- Monitoramento de eventos em diretórios utilizando a biblioteca Watchdog.
- Programação orientada a eventos (POO).
- Utilização de classes e herança.
- Manipulação de arquivos e diretórios.
- Identificação da extensão de arquivos.
- Criação automática de diretórios.
- Movimentação de arquivos entre diretórios.
- Verificação da existência de arquivos e pastas.
- Tratamento de interrupções com try/except.
- Geração de números aleatórios para evitar conflitos de nomes.

## ⚙️ Funcionalidades
- Monitora automaticamente a pasta de Downloads.
- Identifica arquivos recém-baixados.
- Classifica arquivos de acordo com sua extensão.
- Organiza imagens, vídeos, documentos e arquivos de instalação em pastas específicas.
- Cria automaticamente as pastas de destino quando necessário.
- Detecta arquivos com nomes duplicados.
- Renomeia arquivos duplicados automaticamente.
- Move os arquivos para suas respectivas pastas.
- Permite interromper o programa utilizando Ctrl + C.
- Exibe no terminal o status das operações realizadas.

## 🛠️ Stack
- Python
- Watchdog
Bibliotecas padrão: `os`, `shutil`, `time` e `random`

## 🚀 Deploy
1. Clone ou baixe este repositório.

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO
```

2. Instale a bibiloteca watchdog, se necessário.
```bash
pip install watchdog
```
3. Configure os diretórios `from_dir` e `to_dir` no código
4. Execute o programa.
```bash
python nome_do_arquivo.py
```
5. Para interromper a execução, pressione `Ctrl + C`.

## ✅ Licença
- **Permissão de Uso:** O código pode ser usado somente para fins educacionais.

- **Modificação e Distribuição:** Qualquer pessoa pode modificar o código e redistribuí-lo, seja na forma original ou modificada, desde que citando autores.

- **Inclusão da Licença:** Ao redistribuir o software, a licença original e o aviso de direitos autorais devem ser incluídos no código fonte ou na documentação, garantindo que futuros usuários conheçam seus direitos.

- **Isenção de Garantia:** O software é fornecido "como está", sem garantias de qualquer tipo, explícitas ou implícitas. Os autores não são responsáveis por quaisquer danos decorrentes do uso do software.

## 👩🏻‍💻 Autor(es)
- [@penelopefarias745](https://github.com/PenelopeFarias745)

