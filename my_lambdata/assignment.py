

import pandas






def add_state_names(my_df):
    """
    ADDS corresponding
    """
    new_df = my_df.copy()
    
    names_map = {
        "CA": "Cali",
        "CT": "Conn",
        "CO": "Colorado",
        "TX": "Texas",
        "DC": "District of Columbia",
        "OH": "Ohio",
        "MI": "Michigan",
        "PA": "Pennslyvania"
    
    }

    new_df["name"] = new_df["abbrev"].map(names_map)
    return new_df

if __name__ == "__main__":

    df = pandas.DataFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    print(df.head())
    new_df = add_state_names(df)
    print(new_df.head())

    print("___________")

    df2 = pandas.DataFrame({"abbrev": ["OH", "MI", "CO", "TX", "PA"]})
    print(df2.head())
    new_df2 = add_state_names(df2)
    print(new_df2.head())
