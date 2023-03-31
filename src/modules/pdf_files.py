from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'
RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)
writer = PdfWriter()

print('pages:',len(reader.pages))
for i, page in enumerate(reader.pages):
	# print(page)
	print('page',page.extract_text())
	for image in page.images:
		print('image:',image)
		with open(PASTA_NOVA / image.name, 'wb') as fp:
			fp.write(image.data)
		
	writer = PdfWriter()	
	with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
		writer.add_page(page)
		writer.write(arquivo) 


writer1 = PdfWriter()
with open(PASTA_NOVA / 'newPDF.pdf', 'wb') as arquivo:
	for page in reader.pages:
		writer1.add_page(page)
	writer1.write(arquivo)


