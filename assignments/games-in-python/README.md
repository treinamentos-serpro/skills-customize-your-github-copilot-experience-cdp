
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Crie o jogo da Forca em Python para praticar cadeias de caracteres, listas, estruturas de repetição, condicionais e entrada de dados. O jogador deve descobrir uma palavra oculta antes de esgotar as tentativas disponíveis.

## 📝 Tarefas

### 🛠️ Selecione a palavra e prepare o estado inicial

#### Descrição

Implemente a seleção aleatória de uma palavra e prepare as informações necessárias para iniciar uma partida.

#### Requisitos

O programa deve:

- Selecionar aleatoriamente uma palavra de uma lista predefinida.
- Manter a palavra oculta durante a partida e exibir uma posição por letra, como `_ _ _ _`.
- Definir e exibir o número de tentativas incorretas disponíveis.

### 🛠️ Implemente os palpites e o fim da partida

#### Descrição

Crie o laço principal para receber palpites de letras, atualizar o progresso e encerrar a partida quando o jogador vencer ou ficar sem tentativas.

#### Requisitos

O programa deve:

- Solicitar uma letra ao jogador e verificar se ela aparece na palavra.
- Revelar todas as posições correspondentes quando o palpite estiver correto.
- Reduzir as tentativas restantes quando o palpite estiver incorreto.
- Encerrar quando todas as letras forem descobertas ou não houver mais tentativas.
- Exibir uma mensagem indicando vitória ou derrota e revelar a palavra ao fim da partida.