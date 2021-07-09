# Frases cômicas dos presidentes do Brasil

Microserviço para servir as frases mais cômicas dos presidentes do Brasil

## mapeamento
retornam a frase formatada em HTML
```
GET /aleatório -> retorna uma frase de qualquer presidente
GET /<presidente>  -> retorna uma frase de o presidente passado, caso ele esteja na lista de presidentes
```

retornam apenas a frase e o Nome do presidente
```
GET /frase/aleatório
GET /frase/<presidente>
```

<br>

No momento hão frases apenas de Dilma, Lula, Temer e Bolsonaro; és livre para contribuir.