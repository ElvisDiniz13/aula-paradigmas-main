/* Definindo os fatos */
pai(jose, maria).
pai(jose, joao).
mae(ana, maria).
mae(ana, joao).
pai(marcos, jose). 
mae(clarice, jose). 
pai(pedro, ana). 
mae(renata, ana).

/* Regra para verificar se alguém é pai de outra pessoa */
eh_pai(Pai, Filho) :- 
    pai(Pai, Filho).

/* Regra para verificar se alguém é mãe de outra pessoa */
eh_mae(Mae, Filho) :- 
    mae(Mae, Filho).

/* Regra para verificar se duas pessoas são irmãos */
irmao(Irmão1, Irmão2) :- 
    pai(Pai, Irmão1), 
    pai(Pai, Irmão2), 
    mae(Mae, Irmão1), 
    mae(Mae, Irmão2), 
    Irmão1 \= Irmão2.

/* Regra para verificar se uma pessoa é avô de outra */
eh_avô(Avô, Neto) :- 
    pai(Avô, Pai), 
    pai(Pai, Neto).
eh_avô(Avô, Neto) :- 
    mae(Avô, Mae), 
    mae(Mae, Neto).

/* Regra para verificar se uma pessoa é avó de outra */
eh_avó(Avó, Neto) :- 
    mae(Avó, Pai), 
    pai(Pai, Neto).
eh_avó(Avó, Neto) :- 
    pai(Avó, Mae), 
    mae(Mae, Neto).
