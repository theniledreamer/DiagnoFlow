import pandas as pd

class MED_TEST:
    class ABR:
        wells_required = 4
        well = {
            1: {
                "KPC": {"reporter": "FAM", "color": (176, 23, 31)},
                "NDM": {"reporter": "ROX", "color": (0, 139, 69)},
                "RNASE P": {"reporter": "CY5", "color": (238, 238, 0)},
                "VIM": {"reporter": "VIC", "color": (0, 0, 255)}
            },
            2: {
                "IMP": {"reporter": "FAM", "color": (139, 137, 112)},
                "OXA": {"reporter": "ROX", "color": (142, 56, 142)},
                "QNR": {"reporter": "VIC", "color": (238, 121, 66)}
            },
            3: {
                "MEC A/ MEC C": {"reporter": "FAM", "color": (0, 245, 255)},
                "VAN A": {"reporter": "VIC", "color": (238, 220, 130)},
                "VAN B": {"reporter": "ROX", "color": (255, 127, 0)}
            },
            4: {
                "BACILLUS (EC)": {"reporter": "CY5", "color": (238, 18, 137)},
                "CTX": {"reporter": "VIC", "color": (51, 161, 201)},
                "DFRA": {"reporter": "ROX", "color": (238, 18, 137)},
                "SUL 1-2": {"reporter": "FAM", "color": (238, 44, 44)}
            }
        }
    class MiniRPP:
        wells_required = 2
        well = {
            1: {
                "FLU A": {"reporter": "VIC", "color": (0, 0, 255)},
                "FLU B": {"reporter": "ROX", "color": (0, 139, 69)},
                "MS2": {"reporter": "CY5", "color": (238, 238, 0)},
                "SARS-COV-2": {"reporter": "FAM", "color": (176, 23, 31)}
            },
            2: {
                "H5N1": {"reporter": "FAM", "color": (139, 137, 112)},
                "RNASE P": {"reporter": "VIC", "color": (238, 121, 66)},
                "RSV A": {"reporter": "ROX", "color": (142, 56, 142)},
                "RSV B": {"reporter": "CY5", "color": (198, 113, 113)}
            }
        }
    class RPP:
        wells_required = 9
        well = {
            1: {
                "FLU A": {"reporter": "VIC", "color": (0, 0, 255)},
                "FLU B": {"reporter": "ROX", "color": (0, 139, 69)},
                "RNASE P": {"reporter": "CY5", "color": (139, 137, 112)},
                "SARS-COV-2": {"reporter": "FAM", "color": (176, 23, 31)}
            },
            2: {
                "CORONAVIRUS 229E": {"reporter": "FAM", "color": (176, 23, 31)},
                "CORONAVIRUS NL63": {"reporter": "ROX", "color": (0, 139, 69)},
                "CORONAVIRUS OC43": {"reporter": "VIC", "color": (0, 0, 255)},
                "RSV A": {"reporter": "CY5", "color": (238, 238, 0)}
            },
            3: {
                "M CATARRHALIS": {"reporter": "VIC", "color": (238, 121, 66)},
                "RSV B": {"reporter": "CY5", "color": (198, 113, 113)},
                "S AUREUS": {"reporter": "ROX", "color": (142, 56, 142)},
                "S PYOGENES": {"reporter": "FAM", "color": (139, 137, 112)}
            },
            4: {
                "HUMAN BOCOVIRUS": {"reporter": "VIC", "color": (238, 220, 130)},
                "HUMAN METAPNEUMOVIRUS": {"reporter": "ROX", "color": (255, 127, 0)},
                "HUMAN RHINOVIRUS": {"reporter": "FAM", "color": (0, 245, 255)},
                "PARAINFLUENZA 1": {"reporter": "CY5", "color": (142, 142, 56)}
            },
            5: {
                "CORONAVIRUS HKU1": {"reporter": "ROX", "color": (238, 18, 137)},
                "ENTEROVIRUS": {"reporter": "VIC", "color": (51, 161, 201)},
                "PARAINFLUENZA 2": {"reporter": "FAM", "color": (238, 44, 44)},
                "PARAINFLUENZA 3": {"reporter": "CY5", "color": (176, 23, 31)}
            },
            6: {
                "ADENVIRUS": {"reporter": "FAM", "color": (0, 0, 255)},
                "EBV": {"reporter": "ROX", "color": (238, 238, 0)},
                "K PNEUMOPHILA": {"reporter": "VIC", "color": (0, 139, 69)},
                "PARAINFLUENZA 4": {"reporter": "CY5", "color": (139, 137, 112)}
            },
            7: {
                "C PNEUMONIAE": {"reporter": "VIC", "color": (142, 56, 142)},
                "L PNEUMOPHILA": {"reporter": "FAM", "color": (238, 121, 66)},
                "M PNEUMONIAE": {"reporter": "ROX", "color": (198, 113, 113)},
                "MS2 (EC)": {"reporter": "CY5", "color": (0, 245, 255)}
            },
            8: {
                "B PERTUSSIS": {"reporter": "ROX", "color": (142, 142, 56)},
                "BACILLUS (EC)": {"reporter": "CY5", "color": (238, 44, 44)},
                "H INFLUENZAE": {"reporter": "FAM", "color": (238, 220, 130)},
                "S PNEUMONIAE": {"reporter": "VIC", "color": (255, 127, 0)}
            },
            9: {
                "FLU A": {"reporter": "VIC", "color": (0, 0, 255)}
            }
        }
    class STI:
        wells_required = 4
        well = {
            1: {
                "HSV 1": {"reporter": "FAM", "color": (176, 23, 31)},
                "HSV 2": {"reporter": "VIC", "color": (0, 0, 255)},
                "RNASE P": {"reporter": "CY5", "color": (238, 238, 0)},
                "S AGALACTIAE": {"reporter": "ROX", "color": (0, 139, 69)}
            },
            2: {
                "CT": {"reporter": "ROX", "color": (142, 56, 142)},
                "GV": {"reporter": "VIC", "color": (238, 121, 66)},
                "T PALLIDUM": {"reporter": "FAM", "color": (139, 137, 112)}
            },
            3: {
                "M HOMINIS": {"reporter": "ROX", "color": (255, 127, 0)},
                "NG": {"reporter": "FAM", "color": (0, 245, 255)},
                "UREAPLASMA SPP": {"reporter": "VIC", "color": (238, 220, 130)}
            },
            4: {
                "BACILLUS (EC)": {"reporter": "CY5", "color": (238, 238, 0)},
                "H DUCREYI": {"reporter": "FAM", "color": (176, 23, 31)},
                "MG": {"reporter": "ROX", "color": (0, 139, 69)},
                "TV": {"reporter": "VIC", "color": (0, 0, 255)}
            }
        }
    class UTI:
        wells_required = 8
        well = {
            1: {
                "E COLI": {"reporter": "FAM", "color": (176, 23, 31)},
                "K OYTOCA": {"reporter": "ROX", "color": (0, 139, 69)},
                "RNASE P": {"reporter": "CY5", "color": (238, 238, 0)},
                "S AGALACTIAE": {"reporter": "VIC", "color": (0, 0, 255)}
            },
            2: {
                "A URINAE": {"reporter": "CY5", "color": (198, 113, 113)},
                "P MIRABILIS": {"reporter": "ROX", "color": (142, 56, 142)},
                "S MARCESCENS": {"reporter": "VIC", "color": (238, 121, 66)},
                "S SAPROPHYTICUS": {"reporter": "FAM", "color": (139, 137, 112)}
            },
            3: {
                "C FREUNDII": {"reporter": "CY5", "color": (142, 142, 56)},
                "E CLOACAE": {"reporter": "VIC", "color": (238, 220, 130)},
                "P AERUGINOSA": {"reporter": "ROX", "color": (255, 127, 0)},
                "T PALLIDUM": {"reporter": "FAM", "color": (0, 245, 255)}
            },
            4: {
                "C UREALYTICUM": {"reporter": "CY5", "color": (176, 23, 31)},
                "K AEROGENES": {"reporter": "FAM", "color": (238, 44, 44)},
                "K PNEUMONIAE": {"reporter": "VIC", "color": (51, 161, 201)},
                "M MORANELLA": {"reporter": "ROX", "color": (238, 18, 137)}
            },
            5: {
                "A BAUMANNII": {"reporter": "ROX", "color": (238, 238, 0)},
                "E FAECALIS": {"reporter": "VIC", "color": (0, 139, 69)},
                "E FAECIUM": {"reporter": "FAM", "color": (0, 0, 255)},
                "P VULGARIS": {"reporter": "CY5", "color": (139, 137, 112)}
            },
            6: {
                "S AUREUS": {"reporter": "FAM", "color": (238, 121, 66)},
                "UREAPLASMA SPP": {"reporter": "ROX", "color": (142, 56, 142)}
            },
            7: {
                "C ALBICANS": {"reporter": "FAM", "color": (198, 113, 113)},
                "C GLABRATA": {"reporter": "VIC", "color": (0, 245, 255)},
                "C PARAPSILOSIS": {"reporter": "ROX", "color": (238, 220, 130)},
                "P STUARTII": {"reporter": "CY5", "color": (255, 127, 0)}
            },
            8: {
                "BACILLUS (EC)": {"reporter": "CY5", "color": (238, 18, 137)},
                "C AURIS": {"reporter": "ROX", "color": (51, 161, 201)},
                "C KRUSEI": {"reporter": "VIC", "color": (238, 44, 44)},
                "C TROPICALIS": {"reporter": "FAM", "color": (142, 142, 56)}
            }
        }