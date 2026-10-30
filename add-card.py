import re

# Ler o arquivo atual
with open('C:/Users/renat/site-renato-penner/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Encontrar a posição do footer
footer_pattern = r'</footer>'
footer_pos = content.find('</footer>')

if footer_pos == -1:
    print('Footer não encontrado')
    exit(1)

# Criar o novo card
new_card = '''
<article class="card" style="background:#161b22;border:1px solid #30363d;border-radius:6px;padding:24px;margin:20px auto;max-width:600px;">
  <h2 style="color:#58a6ff;margin-top:0;">Promoção do dia</h2>
  <p style="color:#8b949e;">Valor: <strong style="color:#58a6ff;">R$ 44,99</strong></p>
  <img src="img/novo-card-44.99.png" style="max-width:100%;border-radius:4px;">
</article>
'''

# Insertar antes do footer
new_content = content[:footer_pos] + new_card + content[footer_pos:]

# Escrever de volta
with open('C:/Users/renat/site-renato-penner/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Card adicionado com sucesso!')
print('Nova imagem: img/novo-card-44.99.png')
print('Valor: R$ 44,99')
