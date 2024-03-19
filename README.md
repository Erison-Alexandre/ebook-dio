
## Aplicação:

Um ebook feito utilizando apenas Chat GPT, Leonardo.AI e Canva.
Os prompts foram, no chat GPT, a solicitação do codigo depois introdução e conclusão, no leonardo foi solicitado imagem de pc com logo do Youtube e depois homens programando e fechando tudo em um modelo do canva.

## Introdução:

O programa desenvolvido é uma aplicação em Python que utiliza as bibliotecas MoviePy e PyTube para baixar vídeos do YouTube e adicionar legendas a eles. Esse programa é útil para aqueles que desejam assistir a vídeos do YouTube com legendas embutidas, seja por necessidade de acessibilidade ou para aprender um novo idioma.

**Conceito Utilizado:**

O conceito principal explorado neste programa é a automação de tarefas de download de vídeo e adição de legendas. A automação de tarefas é uma prática comum na programação, onde rotinas repetitivas são automatizadas por meio de scripts ou programas. Neste caso, a automação é aplicada ao processo de baixar um vídeo do YouTube, procurar e baixar a legenda correspondente (se disponível) e finalmente combinar o vídeo e a legenda em um único arquivo de vídeo.

Além disso, o programa utiliza APIs fornecidas pelas bibliotecas PyTube e MoviePy para interagir com o YouTube e manipular arquivos de vídeo, respectivamente. Isso demonstra a importância de utilizar bibliotecas e APIs em vez de reinventar a roda, aproveitando o trabalho de desenvolvedores especializados para alcançar os objetivos de programação de forma eficiente e eficaz.

## Passo a Passo Detalhado:

1. **Importação de bibliotecas:**

   ```python
   import os
   from pytube import YouTube
   from moviepy.editor import VideoFileClip
   from moviepy.editor import TextClip
   ```
   - `os`: é usado para interagir com o sistema operacional, manipulando caminhos de arquivos e pastas.
   - `pytube.YouTube`: é a classe fornecida pelo PyTube para interagir com vídeos do YouTube.
   - `moviepy.editor.VideoFileClip`: é usada para carregar vídeos e realizar operações de edição de vídeo.
   - `moviepy.editor.TextClip`: é usada para criar um clip de texto que será usado como legenda.

2. **Função `download_video(url, output_path)`**:
   
   Esta função baixa o vídeo do YouTube com a URL fornecida para o caminho de saída especificado. Ele tenta baixar o vídeo em formato MP4 com resolução de 360p.

3. **Função `download_subtitle(youtube_url, output_path)`**:

   Esta função baixa a legenda em português (se disponível) para o vídeo do YouTube. Se a legenda for encontrada, ela é salva em um arquivo SRT.

4. **Função `add_subtitle(video_path, subtitle_path, output_path)`**:

   Esta função carrega o vídeo baixado e o arquivo de legenda, cria um clip de texto a partir da legenda e adiciona esse clip ao vídeo. O vídeo resultante com a legenda é salvo no caminho de saída especificado.

5. **Função `main()`**:

   Esta função principal controla o fluxo do programa. Ela solicita a URL do vídeo do usuário e o caminho da pasta de saída. Em seguida, chama as funções para baixar o vídeo, baixar a legenda e adicionar a legenda ao vídeo. Se a operação for bem-sucedida, imprime uma mensagem com o caminho do vídeo resultante. Se ocorrer um erro, imprime uma mensagem correspondente.

6. **Execução do programa**:

   ```python
   if __name__ == "__main__":
       main()
   ```
   - Esta linha garante que o programa seja executado somente se for executado como um script principal. Isso impede que o código seja executado se o arquivo for importado como um módulo em outro script.

## Conclusão:

Este projeto proporcionou uma oportunidade de explorar a automação de tarefas em Python, utilizando bibliotecas como PyTube e MoviePy para baixar vídeos do YouTube e adicionar legendas a eles. Ao longo do desenvolvimento, aprendemos a importância de utilizar APIs e bibliotecas de terceiros para facilitar o desenvolvimento de soluções eficazes e eficientes.

A automação de tarefas é uma habilidade valiosa em diversas áreas, incluindo produção de conteúdo, análise de dados, gerenciamento de sistemas e muito mais. Neste projeto específico, vimos como a automação pode ser aplicada para simplificar o processo de assistir a vídeos do YouTube com legendas incorporadas, melhorando a acessibilidade e facilitando a aprendizagem de novos idiomas.

Além disso, ao utilizar bibliotecas Python como PyTube e MoviePy, compreendemos a importância de aproveitar o vasto ecossistema de bibliotecas disponíveis na comunidade Python. Isso não apenas acelera o desenvolvimento de soluções, mas também nos permite concentrar nossos esforços na lógica específica do problema que estamos resolvendo.

Em resumo, este projeto exemplifica como a automação de tarefas pode ser aplicada de forma prática e útil, destacando a importância de utilizar bibliotecas e APIs para alcançar nossos objetivos de programação de maneira eficiente. Essas habilidades são essenciais para qualquer desenvolvedor que busque criar soluções eficazes e automatizar processos repetitivos em suas áreas de atuação.
```
