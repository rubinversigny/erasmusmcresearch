#!/bin/bash

abricate *.fasta > resultncbi.tab --db ncbi --debug 

abricate *.fasta > resultscard.tab --db card --debug 

abricate *.fasta > resultsresfinder.tab --db resfinder --debug 

abricate --summary resultsncbi.tab > summaryncbi.tab 

abricate --summary resultscard.tab > summarycard.tab 

abricate --summary resultsresfinder.tab > summaryresfinder.tab 

done 