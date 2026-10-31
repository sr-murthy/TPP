Repository of Code and Data for the TPP Triples Computational Search Project
============================================================================

The [GAP system](https://www.gap-system.org/) code and data in this repository are related to an extensive computational search project for triple product property (TPP) triples of finite groups carried out in 2011-2012 as part of a research project for the jointly-authored and published paper with I. Hedkte:

I. Hedtke and S. Murthy, 'Search and test algorithms for triple product property triples', *Groups - Complexity - Cryptology*, 4(1): 111-133, 2012. DOI: [https://doi.org/10.1515/gcc-2012-0006](https://doi.org/10.1515/gcc-2012-0006)

Objectives
----------

The paper focused on determining:

* TPP capacity $\beta$ (maximally sized TPP triples) in *all* finite groups of order 1-32.
* Subgroup TPP capacity $\beta_0$ (maximally sized TPP triples of subgroups) in *all* finite groups of order 1-1000, except for groups of order 512 and 768 (and some other orders), which were omitted for computational and logistical reasons.

Abelian groups were not actually searched as their TPP and subgroup TPP capacities are known and trivial, and in fact only nonabelian groups were searched, but they are included in the dataset for reasons of completion.

Code & Data
-----------

The code and data in this repository can be found across a number of folders, primarily:

* `TPP/TPP` - the code for the Django app that was setup to make the data accessible
* `TPP/assets` - the main contents are HTML pages containing tables of the subgroup TPP search data, organised by group order ranges, and the GAP code for writing these tables
* `TPP_App/lib` - Python wrapper code for parsing the raw search data from GAP
* `TP_App/static` - the main contents are essentially JSON versions of the raw subgroup TPP search data contained in the HTML tables in `TPP/assets`

In 2026 the author created a single "master" CSV file, [`master_subgroup_tpp_data.csv`](https://github.com/sr-murthy/TPP/blob/master/TPP/master_subgroup_tpp_data.csv), for the subgroup TPP search data from the individual JSON files, containing a total of 49024 entries. The CSV is stored in the top-level `TPP` subfolder. The columns of the CSV are briefly described below (in order of occurrence):

* `'order'` - the order $|G|$ of the group.
* `'gap_id'` - the GAP ID of the group in the format `'[<order>, <small group lib. no.>]'`.
* `'gap_desc'` - the GAP structure description of the small group.
* `'beta0'` - the subgroup TPP capacity $\beta_0(G) \geq |G|$ of the group $G$.
* `'rho0'` - the subgroup TPP ratio $\rho_0(G) = \frac{\beta_0(G)}{|G|} \geq 1$ of the group $G$.
* `'mbs_tpp_params'` - the parameters (or parameter type) $(|S|, |T|, |U|)$ of a (not necessarily unique) maximal-by-size (MBS) subgroup TPP triple $(S, T, U)$ of $G$. This means that $S, T, U$ are subgroups of $G$ satisfying the TPP and $\frac{|S||T||U|}{|G|} = \rho_0(G)$.
* `'group_gens'` - a list of generators of $G$, given as a list of pairs, each pair consisting of a generator and its group order.
* `'is_abelian'` - whether $G$ is abelian.
* `'is_elem_abelian'` - whether $G$ is elementary abelian.
* `'is_cyclic'` - whether $G$ is cyclic.
* `'index_lan_subgroup'` - index of a largest abelian normal subgroup of $G$.
* `'index_lean_subgroup'` - index of a largest elementary abelian normal subgroup of $G$.
* `'index_lcn_subgroup'` - index of a largest cyclic normal subgroup of $G$.
* `'is_pgroup'` - whether $G$ is a $p$-group (a group of prime power order for some prime $p$).
* `'is_simple'` - whether $G$ is a simple group (contains no nontrivial normal subgroups besides the trivial group $\{1\}$ and $G$ itself).
* `'composition_length'` - the length of a composition series of $G$.
* `'is_nilpotent'` - whether $G$ is nilpotent, in the sense of having a central series of finite length.
* `'nilpotency_class'` - the nilpotency class of $G$, if $G$ is in fact nilpotent.
* `'is_solvable'` - whether $G$ is a solvable group, in the sense of having a derived/commutator series that terminates in the trivial group $\{1\}$.
* `'commutator_length'` - the commutator length of $G$ (the smallest $n \geq 1$ such that each element in the commutator subgroup $G' = [G, G]$ can be written as a product of at most $n$
commutators of elements in G).
* `'derived_length'` - the derived length of $G$ **if** it is solvable (the length of the derived series of $G$ **when $G$ is solvable**).
* `'character_degrees'` - the multiset $\{\chi(1) \mathrel | \chi \in \text{Irr}(G)\}$ of (complex, irreducible) character degrees of $G$.
* `'D3'` - the quantity $D_3(G) = \sum_{\chi \in \text{Irr}(G)} \chi(1)^3$ of the character degrees of $G$ (also called the $3$-character capacity of $G$).

Search Software & Infrastructure
--------------------------------

The TPP test and search code was written in the [GAP system](https://www.gap-system.org/) language, but the repository does not contain this code as it is no longer accessible by the author. But it can be inferred from the very clear descriptions of the underlying test and search algorithms given in the paper above.

The GAP system version used for this particular project was 4.4.12 (2008).

The code was executed on supercomputers at the Friedrich Schiller University, Jena and the Martin Luther University, Halle-Wittenberg in Germany during 2011-2012, but this author also tested and ran parts of the code locally on a 2011 MacBook Air.

Background & Further References
-------------------------------

The original paper introducing TPP triples can be found here:

* H. Cohn and C. Umans, 'A group-theoretic approach to fast matrix multiplication', in: *Proceedings of the 44th Annual Symposium on Foundations of Computer Science* (Cambridge, Massachusetts 2003), IEEE Computer Society (2003), 438-449. DOI: [https://dl.acm.org/doi/10.5555/946243.946301](https://dl.acm.org/doi/10.5555/946243.946301)

Further papers and preprints on this topic involving the author are listed below (in descending chronological order):

* S. R. Murthy, 'On the triple product property for subgroups of finite groups of nilpotency class 2', arXiv:2602.15796, 2026. DOI: [https://doi.org/10.48550/arXiv.2602.15796](https://doi.org/10.48550/arXiv.2602.15796)

* S. R. Murthy, 'A note on the triple product property for finite groups with abelian normal subgroups of prime index', arXiv:2512.16730, 2025. DOI: [https://doi.org/10.48550/arXiv.2512.16730](https://doi.org/10.48550/arXiv.2512.16730)

* S. Hart, I. Hedtke, M. Müller-Hannemann and S. Murthy, 'A fast search algorithm for TPP triples and an application for 5 x 5 matrix multiplication', *Groups - Complexity - Cryptology*, 7(1): 31-46, 2015. DOI: [https://doi.org/10.1515/gcc-2015-0001](https://doi.org/10.1515/gcc-2015-0001)
