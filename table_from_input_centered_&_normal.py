from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    

    #Create Box Parts
    vertical = "│"
    horizontal = "─" 
    left_upper_corner = "┌"
    col_upper_partition = "┬"
    right_upper_corner = "┐"
    left_row_partition = "├"
    mid_row_partition = "┼"
    right_row_partition = "┤"
    left_lower_corner = "└"
    col_lower_partition = "┴"
    right_lower_corner = "┘"

    #Convert Every row to str
    rows = [list(map(str,row)) for row in rows]
    
    #Check number of columns
    col_length=len(rows[0])
    tab = left_upper_corner
    cell_width=[0 for i in range (col_length)]

#calculate Cell-Width 

    #If Label none
    for i in range (col_length):
    	for row in rows:
    		cell_width[i] = len(row[i]) if cell_width[i]<len(row[i]) else cell_width[i]

    #If Label is not null
    if labels is not None:
    	for i in range(len(labels)):
    		cell_width[i] = len(labels[i]) if cell_width[i]<len(labels[i]) else cell_width[i]




    #Create "┌────────────┬───────────┬─────────┐"

    for i in range(col_length):
    	tab += f'{horizontal}'*(cell_width[i]+2)+f"{col_upper_partition}"
    tab = tab[:-1]

    tab += f"{right_upper_corner}\n"

    #Labels Printing
    tab += f'{vertical}'
    if labels is not None:
    	j = 0
    	for label in labels:
    		remaining_spaces = cell_width[j]-len(label)
    		if centered is not True:
	    		tab += f' {label}' + ' '*remaining_spaces + f' {vertical}'
	    		j +=1
	    	else:
	    		left_space = int(remaining_spaces/2)
    			right_space = remaining_spaces - left_space
    			tab += ' '*left_space + f' {label}' + ' '*right_space + f' {vertical}'
    			j+=1
    	tab += "\n"

    #Create "├────────────┼───────────┼─────────┤" After labels
    tab += f'{left_row_partition}'
    for i in cell_width:
    	tab += f'{horizontal}'*(i+2) + f'{mid_row_partition}'
    tab = tab[:-1]
    tab += f'{right_row_partition}\n'



    #Rows Printing
    for row in rows:
    	tab += f'{vertical}'
    	j=0
    	for i in row:
    		remaining_spaces = cell_width[j]-len(i)
    		if centered is not True:
    			tab += f' {i}'+' '*remaining_spaces+f' {vertical}'
    			j+=1
    		else:
    			left_space = int(remaining_spaces/2)
    			right_space = remaining_spaces - left_space
    			tab += ' '*left_space + f' {i}' + ' '*right_space + f' {vertical}'
    			j+=1
    	tab += "\n"

	#Create Footer "└────────────┴───────────┴─────────┘"

    tab += f"{left_lower_corner}"
    for i in range (col_length):
    	tab += f"{horizontal}"*(cell_width[i]+2) +f'{col_lower_partition}'
    tab = tab[:-1]
    tab+=f'{right_lower_corner}'
    return tab


table = make_table(
	rows=[
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"],
                    ["Hippopotomonstrosesquippedaliophobia"],
                    ["Supercalifragilisticexpialidocious"],
                    ["Pseudopseudohypoparathyroidism"],
                    ["Floccinaucinihilipilification"],
                    ["Antidisestablishmentarianism"],
                    ["."]
                ],
                labels=["My Favourite Long Words"],
                centered=True
)
print(table)