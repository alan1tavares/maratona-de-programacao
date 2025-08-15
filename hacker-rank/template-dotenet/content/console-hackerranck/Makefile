all: run test

run:
	@rm -f ./output.txt
	@OUTPUT_PATH=./output.txt dotnet run < ./input.txt

test:
	@echo "Comparando a saída com a saída esperada..."
	@git --no-pager diff --no-index --color-words --word-diff-regex=. \
		./expected_output.txt ./output.txt
	@echo "Os arquivos são iguais"