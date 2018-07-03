# Toolbox Duplicate Finder

Identify duplicate tools in your Galaxy toolbox

## Running it

```
curl --silent https://usegalaxy.eu/api/tools | python3 asdf.py
```

## Output

Repo | Tool | Sections
---- | ---- | --------
bgruening/deeptools_bam_compare          | bamCompare                     | Epigenetics, deepTools
bgruening/deeptools_bam_coverage         | bamCoverage                    | Epigenetics, deepTools
bgruening/deeptools_bam_pe_fragmentsize  | bamPEFragmentSize              | Epigenetics, deepTools
bgruening/deeptools_bigwig_compare       | bigwigCompare                  | Epigenetics, deepTools
bgruening/deeptools_compute_gc_bias      | computeGCBias                  | Epigenetics, deepTools
bgruening/deeptools_compute_matrix_operations | computeMatrixOperations        | Epigenetics, deepTools
bgruening/deeptools_compute_matrix       | computeMatrix                  | Epigenetics, deepTools
bgruening/deeptools_correct_gc_bias      | correctGCBias                  | Epigenetics, deepTools
bgruening/deeptools_multi_bam_summary    | multiBamSummary                | Epigenetics, deepTools
bgruening/deeptools_multi_bigwig_summary | multiBigwigSummary             | Epigenetics, deepTools
bgruening/deeptools_plot_correlation     | plotCorrelation                | Epigenetics, deepTools
bgruening/deeptools_plot_coverage        | plotCoverage                   | Epigenetics, deepTools
bgruening/deeptools_plot_enrichment      | plotEnrichment                 | Epigenetics, deepTools
bgruening/deeptools_plot_fingerprint     | plotFingerprint                | Epigenetics, deepTools
bgruening/deeptools_plot_heatmap         | plotHeatmap                    | Epigenetics, deepTools
bgruening/deeptools_plot_pca             | plotPCA                        | Epigenetics, deepTools
bgruening/deeptools_plot_profile         | plotProfile                    | Epigenetics, deepTools
bgruening/glimmer3                       | Glimmer3                       | Annotation, Annotation
bgruening/hicup_deduplicator             | Hicup Deduplicator             | Epigenetics, deepTools
bgruening/protease_prediction            | Protease prediction            | Proteomics, Proteomics
bgruening/text_processing                | Replace Text                   | Text Manipulation, Text Manipulation
devteam/basecoverage                     | Base Coverage                  | Text Manipulation, Operate on Genomic Intervals
devteam/bowtie2                          | Bowtie2                        | Mapping, deepTools
devteam/cluster                          | Cluster                        | Text Manipulation, Operate on Genomic Intervals
devteam/complement                       | Complement                     | Text Manipulation, Operate on Genomic Intervals
devteam/dgidb_annotator                  | Annotate with DGI              | Annotation, Annotation
devteam/fasta_to_tabular                 | FASTA-to-Tabular               | Convert Formats, FASTA/FASTQ manipulation
devteam/fastq_stats                      | FASTQ Summary Statistics       | FASTA/FASTQ manipulation, Quality Control
devteam/fastq_to_fasta                   | FASTQ to FASTA                 | Convert Formats, FASTA/FASTQ manipulation
devteam/fastqtofasta                     | FASTQ to FASTA                 | Convert Formats, FASTA/FASTQ manipulation
devteam/fastx_nucleotides_distribution   | Draw nucleotides distribution chart | FASTA/FASTQ manipulation, Quality Control
devteam/scatterplot                      | Scatterplot                    | Graph/Display Data, Graph/Display Data
devteam/subtract                         | Subtract                       | Text Manipulation, Join, Subtract and Group
devteam/tabular_to_fasta                 | Tabular-to-FASTA               | Convert Formats, FASTA/FASTQ manipulation
devteam/xy_plot                          | Plotting tool                  | Graph/Display Data, Graph/Display Data
galaxyp/idpquery                         | idpQuery                       | Convert Formats, Proteomics
hammock/hammock                          | Hammock - cluster peptides     | Multiple Alignments, Annotation
hgv_add_scores                           | phyloP                         | Phenotype Association, Evolution
hgv_codingSnps                           | aaChanges                      | Phenotype Association, Evolution
iuc/annotatemyids                        | annotateMyIDs                  | Annotation, Annotation
iuc/bedtools                             | AnnotateBed                    | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | BAM to BED                     | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | BED to BAM                     | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | BED to IGV                     | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | BED12 to BED6                  | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | BEDPE to BAM                   | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | ClosestBed                     | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | ClusterBed                     | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | ComplementBed                  | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | Compute both the depth and breadth of coverage | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | Convert from BAM to FastQ      | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | ExpandBed                      | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | FisherBed                      | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | FlankBed                       | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | Genome Coverage                | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | GetFastaBed                    | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | GroupByBed                     | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | Intersect intervals            | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | JaccardBed                     | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | LinksBed                       | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | MakeWindowsBed                 | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | MapBed                         | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | MaskFastaBed                   | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | Merge BedGraph files           | BED Tools, Operate on Genomic Intervals, Operate on Genomic Intervals
iuc/bedtools                             | MergeBED                       | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | MultiCovBed                    | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | Multiple Intersect             | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | NucBed                         | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | OverlapBed                     | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | RandomBed                      | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | ReldistBed                     | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | ShuffleBed                     | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | SlopBed                        | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | SortBED                        | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | SpacingBed                     | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | SubtractBed                    | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | TagBed                         | BED Tools, Operate on Genomic Intervals
iuc/bedtools                             | WindowBed                      | BED Tools, Operate on Genomic Intervals
iuc/fasta_nucleotide_color_plot          | Fasta nucleotide color plot    | Graph/Display Data, Graph/Display Data, Graph/Display Data
iuc/gemini_actionable_mutations          | GEMINI actionable_mutations    | Gemini Tools, Gemini Tools
iuc/gemini_amend                         | GEMINI amend                   | Gemini Tools, Gemini Tools
iuc/gemini_annotate                      | GEMINI annotate                | Gemini Tools, Gemini Tools
iuc/gemini_burden                        | GEMINI burden                  | Gemini Tools, Gemini Tools
iuc/gemini_comp_hets                     | GEMINI comp_hets               | Gemini Tools, Gemini Tools
iuc/gemini_db_info                       | GEMINI db_info                 | Gemini Tools, Gemini Tools
iuc/gemini_de_novo                       | GEMINI de_novo                 | Gemini Tools, Gemini Tools
iuc/gemini_dump                          | GEMINI dump                    | Gemini Tools, Gemini Tools
iuc/gemini_fusions                       | GEMINI fusions                 | Gemini Tools, Gemini Tools
iuc/gemini_gene_wise                     | GEMINI gene_wise               | Gemini Tools, Gemini Tools
iuc/gemini_interactions                  | GEMINI interactions            | Gemini Tools, Gemini Tools
iuc/gemini_load                          | GEMINI load                    | Gemini Tools, Gemini Tools
iuc/gemini_lof_sieve                     | GEMINI lof_sieve               | Gemini Tools, Gemini Tools
iuc/gemini_mendel_errors                 | GEMINI mendel_errors           | Gemini Tools, Gemini Tools
iuc/gemini_pathways                      | GEMINI pathways                | Gemini Tools, Gemini Tools
iuc/gemini_qc                            | GEMINI qc                      | Gemini Tools, Gemini Tools
iuc/gemini_query                         | GEMINI query                   | Gemini Tools, Gemini Tools
iuc/gemini_recessive_and_dominant        | GEMINI autosomal recessive/dominant | Gemini Tools, Gemini Tools
iuc/gemini_region                        | GEMINI region                  | Gemini Tools, Gemini Tools
iuc/gemini_roh                           | GEMINI roh                     | Gemini Tools, Gemini Tools
iuc/gemini_set_somatic                   | GEMINI set_somatic             | Gemini Tools, Gemini Tools
iuc/gemini_stats                         | GEMINI stats                   | Gemini Tools, Gemini Tools
iuc/gemini_windower                      | GEMINI windower                | Gemini Tools, Gemini Tools
iuc/jbrowse                              | JBrowse                        | Graph/Display Data, Graph/Display Data
iuc/jbrowse                              | JBrowse - Data Directory to Standalone | Graph/Display Data, Graph/Display Data
iuc/samtools_sort                        | sort                           | SAM Tools, SAM Tools
iuc/snpeff                               | SnpEff                         | Variant Calling, Annotation
iuc/snpeff                               | SnpEff Download                | Variant Calling, Annotation
jjohnson/query_tabular                   | Query Tabular                  | Filter and Sort, Proteomics
mmonsoor/probmetab                       | ProbMetab Tool                 | Annotation, Metabolomics
peterjc/sample_seqs                      | Sub-sample sequences files     | Filter and Sort, NCBI Blast
pjbriggs/trimmomatic                     | Trimmomatic                    | FASTA/FASTQ manipulation, Quality Control
prog/lcmsmatching                        | LC/MS matching                 | Annotation, Metabolomics
sauria/hifive                            | hifive                         | Epigenetics, Test Tools

## LICENSE

GPL-3
