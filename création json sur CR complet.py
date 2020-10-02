# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:29:43 2020

@author: BL80FB0N
"""

Tree = {
        "name" : 'Compte annuel complet', "children" : {
            "ResultatExploitation" : {"name" : 'Produits d\'exploitation ', "bundle": 10, "liasse": "FR", "children" : {
                "ChiffresAffairesNet" : {"name" : 'Chiffres d\'affaires nets ', "bundle": 4, "liasse": "FJ", "children" : {
                    "VenteMarchandises" : {"name": 'Ventes de marchandises ', "bundle": 1, "liasse": "FA"},
                    "ProductionVendueDeBiens" : {"name": 'Production vendues de biens ', "bundle": 2, "liasse": "FD"},
                    "ProductionVendueDeServices" : {"name": 'Production vendue de services ', "bundle": 3, "liasse": "FG"}
                        }
                    },
                "ProductionStocked" : {"name": 'Production stockée ', "bundle": 5, "liasse": "FM"},
                "ProductionImmobilisee" : {"name": 'Production immobilisée ', "bundle": 6, "liasse": "FN"},
                "SubventionsExploitation" : {"name": 'Subvention d\'exploitation ', "bundle": 7, "liasse": "FO"},
                "RepriseDepreciationProvisionsTransfertChargesExploitation" : {"name": 'Reprises sur dépréciations, provisions (et amortissements), transfert de charges ', "bundle": 8, "liasse": "FP"},
                "AutresProduits" : {"name": 'Autres produits ', "bundle": 9, "liasse": "FQ"}
                },
            "ChargesExploitation" : {"name" : 'Charges d\'exploitation ', "sign" : -1, "bundle": 20, "liasse": "GG", "children" : {
                "AchatsDeMarchandises" : {"name": 'Achats de marchandise (y compris droits de douane)', "bundle": 11, "liasse": "FS"},
                "VariationStockMarchandises" : {"name": 'Variation de stock (marchandises)', "bundle": 12, "liasse": "FT"},
                "AchatMatierePremiereAutreAppro" : {"name": 'Achat de matières premières et autres approvisionnements (et droit de douane)', "bundle": 13, "liasse": "FU"},
                "VariationStockMatierePremiereEtAppro" : {"name": 'Variation de stock (matières premières et approvisionnements)', "bundle": 14, "liasse": "FV"},
                "AutresAchatEtChargesExternes" : {"name": 'Autres achats et charges externes ', "bundle": 15, "liasse": "FW"},
                "ImpotTaxesEtVersementsAssimiles" : {"name": 'Impôts, taxes et versements assimilés ', "bundle": 16, "liasse": "FX"},
                "SalairesEtTraitements" : {"name": 'Salaires et traitements ', "bundle": 17, "liasse": "FY"},
                "ChargesSociales" : {"name": 'Cotisations sociales ', "bundle": 18, "liasse": "FZ"},
                "DotationExploitation" : {"name" : 'DOTATIONS D\'EXPLOITATION ', "children" : {
                    "DotationAmortissementImmobilisations" : {"name": 'Sur immobilisations : dotations aux amortissements '},
                    "DotationDepreciationImmobilisations" : {"name": 'Sur immobilisations : dotations aux dépréciations '},
                    "DotationDepreciationActifCirculant" : {"name": 'Sur actif circulant : dotations aux dépréciations '},
                    "DotationProvisions" : {"name": 'Dotations aux provisions '}
                            }
                        },
                "AutresCharges" : {"name": 'Autres charges ', "bundle": 19, "liasse": "GE"}
                        }
                    }
                },
            "ResultatFinancier" : {"name" : 'Résultat financier ', "bundle": 36, "liasse": "GV", "children" : {
                "ProduitsFinanciers" : {"name" : 'Produits financiers ', "bundle": 30, "liasse": "GQ", "children" : {
                    "ProduitsFinanciersParticipations" : {"name": 'Produits financiers de participations', "bundle": 24, "liasse": "GJ"},
                    "ProduitsAutresValeursMobiliereEtCreancesActifImmobilise" : {"name": 'Produits des autres valeurs mobilières et créances de l\'actif immobilisé', "bundle": 25, "liasse": "GK"},
                    "AutreInteretEtProduitAssimile" : {"name": 'Autres intérêts et produits assimilés', "bundle": 26, "liasse": "GL"},
                    "RepriseDepreciationEtProvisionTransfertsChargesFinancier" : {"name": 'Reprises sur dépréciations et provisions, transferts de charges', "bundle": 27, "liasse": "GM"},
                    "DifferencesPositivesChange" : {"name": 'Différences positives de change', "bundle": 28, "liasse": "GN"},
                    "ProduitsNetsCessionsValeursMobilesPlacement" : {"name": 'Produits nets sur cessions de valeurs mobilières de placement', "bundle": 29, "liasse": "GO"}
                        },
                    },
                "ChargesFinancieres" : {"name" : 'Charges financières ', "sign" : -1, "bundle": 35, "liasse": "GU", "children" : {
                    "DotationsFinancieresAmortissementDepreciationProvision" : {"name": 'Dotations financières aux amortissements, dépréciations et provisions', "bundle": 31, "liasse": "GQ"},
                    "InteretEtChargeAssimilees" : {"name": 'Intérêts et charges assimilées', "bundle": 32, "liasse": "GR"},
                    "DifferenceNegativeChange" : {"name": 'Différences négatives de change', "bundle": 33, "liasse": "GS"},
                    "ChargesNetteCessionValeurMobiliereDePlacement" : {"name": 'Charges nettes sur cessions de valeurs mobilières de placement', "bundle": 34, "liasse": "GT"}
                            }
                        }
                    }
                },
            "ResultatExceptionnel" : {"name" : 'Résultat exceptionnel ', "bundle": 46, "liasse": "HI", "children" : {
                "ProduitsExceptionnels" : {"name" : 'Produits exceptionnels ', "bundle": 41, "liasse": "HD", "children" : {
                    "ProduitExceptionnelOperationCapital" : {"name": 'Produits exceptionnels sur opérations en capital', "bundle": 39, "liasse": "HB"},
                    "ProduitExceptionnelOperationGestion" : {"name": 'Produits exceptionnels sur opérations de gestion', "bundle": 38, "liasse": "HA"},
                    "RepriseDepreciationProvisionTransfertChargeExceptionnel" : {"name": 'Reprises sur dépréciations et provisions, transferts de charges', "bundle": 40, "liasse": "HC"}
                        }
                    },
                "ChargesExceptionnelles" : {"name" : 'Charges exceptionnelles ', "sign" : -1, "bundle": 45, "liasse": "HH", "children" : {
                    "ChargesExceptionnelleOperationGestion" : {"name": 'Charges exceptionnelles sur opérations de gestion', "bundle": 42, "liasse": "HE"},
                    "ChargesExceptionnelleOperationCapital" : {"name": 'Charges exceptionnelles sur opérations en capital', "bundle": 43, "liasse": "HF"},
                    "DotationExceptionnelleAmortissementDepreciationProvision" : {"name": 'Dotations exceptionnelles aux amortissements, dépréciations et provisions', "bundle": 44, "liasse": "HG"},
                            }
                        }
                    }
                },
            "ParticipationSalariesAuxResultats" : {"name": 'Participation des salarié⋅es aux résultats de l\'entreprise ', "sign" : -1 , "bundle": 47, "liasse": "HJ", "children" :{
                    "ImpotsSurLesBenefices" : {"name" : 'Impôts sur les bénéfices ', "sign" : -1 , "bundle": 48, "liasse": "HK"}
                    }
                }
            }
        }
    
print(Tree)


# Il manque Bénéfice attribué ou perte transférée, bundle 22
# Il manque Bénéfice attribué ou perte supportée, bundle 23
# Il manque Résultat en cours avant impôts, bundle 37
# Il manque "Total des produits", bundle 49
# Il manque tous les bundle à partir de 50


