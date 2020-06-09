# Lab-Scripts
# Primer_finder
Introduction:
This code was built to obtain primers for gene silencing protocols. As the FASTA and GFF files are read, this code generates both the upstream and downstream primers which already contain the antibiotic resistance cassette. This cassette was obtained from "A Short Protocol for Gene Knockout and Complementation in Xylella fastidiosa Shows that One of the Type IV Pilin Paralogs (PD1926) Is Needed for Twitching while Another (PD1924) Affects Pilus Number and Location" (Kandel et al. 2018) The construction of these primers was intended to follow the procedure that was outlined in the paper.
The code is comprised of five parts. 

Part 1.

The purpose of this section is to identify which positions are related to the information we need to use in order to obtain the constructs. For this section, the gff file will be used. Using the code, the output will show all of the information of one specific gene including its name, the section of the genome in which it is located, a +/- which states if the gene is in the forward or reverse orientation, and the end and start position. The output of this section is ‘geneinfo’. It should be noted that for this step it is important to know the name of the gene that’s being studied.
Example:
{'gumD': ['Chromosome', '-', '1617908', '1619362']}

Part 2.

This part of the script is a for loop that reads all the FASTA file and uses the information from the output in Part 1 to obtain the nodes in which each gene is located. The output is an updated version of ‘geneinfo’,  in which entire node in which the gene is contained was added.
 
Part 3.  

The outcome for this part of the script is the construct of the gene. The dictionary called ‘constructdictionary’ contains the upstream, and downstream constructs and a +/- indicating if the gene is in the forward or reverse orientation. These constructs are 500 base pairs long. The upstream constructs start 450 base pairs before the start position of the gene and end 50 base pairs after the start position. The downstream construct begins 50 base pairs before the end position of the gene and extends 450 base pairs after said position.
If a gene is in reverse orientation, then the script will change it to the forward orientation. 
An error may occur when the genes are too close to the beginning or the end of the node. The gene must be at least 450 base pairs away from these positions in order to obtain the constructs.

Part 4 . 

The outcome of this portion of the script are the constructs with and without the Kanamycin resistance cassette.

Part 5.

This portion of the script creates files with the primers in the specified position of the constructs. The names of the positions were exactly as seen in Fig. S2 of the knockout protocol (Kandel)
The positions are the following:
Up_F: upstream and in the furthest location relative to the gene of interest (GOI), forward direction
Up_F: upstream  and in the closest location relative to GOI,  reverse direction
Kan_Up_R: kanamycin resistance cassette with  gene  upstream to GOI in the reverse direction.
Kan_Dn_F:  kanamycin resistance cassette with gene downstream to GOI in the forward direction.
Dn_F: Downstream, and in and in the closest location relative to GOI in the forward direction.
Dn_R: Downstream, and in the furthest location relative to  to GOI in the reverse direction

