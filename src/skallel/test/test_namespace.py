import skallel


def test_namespace():

    # Imports from skallel_tensor.
    assert callable(skallel.genotypes_locate_hom)
    assert callable(skallel.genotypes_locate_het)
    assert callable(skallel.genotypes_locate_call)
    assert callable(skallel.genotypes_count_alleles)
    assert callable(skallel.genotypes_to_called_allele_counts)
    assert callable(skallel.genotypes_to_missing_allele_counts)
    assert callable(skallel.genotypes_to_allele_counts)
    assert callable(skallel.genotypes_to_allele_counts_melt)
    assert callable(skallel.genotypes_to_major_allele_counts)
    assert callable(skallel.genotypes_to_haplotypes)
    assert callable(skallel.allele_counts_to_frequencies)
    assert callable(skallel.allele_counts_allelism)
    assert callable(skallel.allele_counts_max_allele)
    assert callable(skallel.variants_to_dataframe)
    assert callable(skallel.select_slice)
    assert callable(skallel.select_indices)
    assert callable(skallel.select_mask)
    assert callable(skallel.select_range)
    assert callable(skallel.select_values)
    assert callable(skallel.concatenate)

    # Imports from skallel_stats.
    assert callable(skallel.pairwise_distance)
