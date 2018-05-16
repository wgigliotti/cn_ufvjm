#!/bin/sh

echo "Processando os textos"
date

# fazendo sim

cat conjunto_treino/ts_sim.csv | ./tokenizeMapper.py | ./stopWordsMapper.py | ./stemmerMapper.py > resultados/ts_sim_proc.csv


cat conjunto_treino/ts_nao.csv | ./tokenizeMapper.py | ./stopWordsMapper.py | ./stemmerMapper.py > resultados/ts_nao_proc.csv

cat conjunto_treino/teste.csv | ./tokenizeMapper.py | ./stopWordsMapper.py | ./stemmerMapper.py > resultados/teste_proc.csv

echo "Construindo vetores de frequencia dos termos"
date
cat resultados/ts_sim_proc.csv | ./tfMapper.py | sort | ./tfReducer.py > resultados/tf_sim.csv
cat resultados/ts_nao_proc.csv | ./tfMapper.py | sort | ./tfReducer.py > resultados/tf_nao.csv
cat resultados/teste_proc.csv | ./tfMapper.py | sort | ./tfReducer.py > resultados/tf_teste.csv


echo "contando Documentos"
date
cat resultados/*proc.csv | wc -l > resultados/numeroDocumentos.csv

echo "Construindo vetores de frequencia de termos em documentos"
date
cat resultados/*proc.csv | ./dfMapper.py | sort | ./dfReducer.py > resultados/document_frequency.csv


cat resultados/tf_sim.csv | ./tfidfMapper.py > resultados/tfidfSim.csv
cat resultados/tf_nao.csv | ./tfidfMapper.py > resultados/tfidfNao.csv
cat resultados/tf_teste.csv | ./tfidfMapper.py > resultados/tfidfTeste.csv
