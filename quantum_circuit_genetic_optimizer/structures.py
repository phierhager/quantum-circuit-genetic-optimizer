from typing import Tuple, TypeAlias, Optional
from dataclasses import dataclass

CnotPair_T: TypeAlias = Tuple[int, int]
GeneSegment_T: TypeAlias = Optional[CnotPair_T]
Gene_T: TypeAlias = list[GeneSegment_T]


@dataclass
class CircuitGene:
    gene: Gene_T
    fitness: float = 0.0

    def __len__(self):
        return len(self.gene)

    def __iter__(self):
        return iter(self.gene)

    def __getitem__(self, index):
        return self.gene[index]
