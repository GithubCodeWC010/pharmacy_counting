f = open("input\itcont.txt", "r") # read the input data on ID's, names, durgs and costs.

last_name = []  # initialize a list of the last names based on the line order they appear in the input file.
first_name = [] # initialize a list of the first names based on the line order they appear in the input file.
drug_name = []  # initialize a list of the drugs based on the line order they appear in the input file.
drug_cost = []  # initialize a list of the drug costs based on the line order they appear in the input file.
for x in f:
        s = x.split(",")        # split the information in each line into smaller sub-strings.
        last_name.append(s[1])  # make a list of the last names based on the line order they appear in the input file.
        first_name.append(s[2]) # make a list of the first names based on the line order they appear in the input file.
        drug_name.append(s[3])  # make a list of the drugs based on the line order they appear in the input file.
        drug_cost.append(s[4])  # make a list of the drug costs on the line order they appear in the input file.

last_name = last_name[1:len(last_name)] # remove the first entry of the list, which corresponds to the first line (titles) in the input data.
first_name = first_name[1:len(first_name)]
drug_name = drug_name[1:len(drug_name)] 
drug_cost = drug_cost[1:len(drug_cost)]

last_first_name = [m+n for m,n in zip(last_name,first_name)] # concatenate the last_name and first_name lists.
list_dis_drug = {x:drug_name.count(x) for x in drug_name} # a dictionary of the list of distinct drugs and the number of times they are prescribed.
g_keys = list(list_dis_drug.keys()) # list of the distinct drugs.

total = []
cnt_per_drug = []
for y in list_dis_drug:
    k = []
    # compute the total cost of each drug across all customers:
    indices = [i for i, x in enumerate(drug_name) if x == y]
    tot = sum([int(drug_cost[i]) for i in indices])
    total.append(tot)

    # compute the number of distinct customers for each drug:
    names_per_drug = [last_first_name[i] for i in indices]
    cnt_temp = {x:names_per_drug.count(x) for x in names_per_drug}
    cnt_per_drug.append(len(cnt_temp))
    
# sort the total cost in a descending order:
j = sorted(enumerate(total), key=lambda x: x[1], reverse=True)

# save the results in the output text file:
file = open("output\output_top_cost_drug.txt", "w")
file.write("drug_name,num_prescriber,total_cost\n")
for i in range(len(j)):
        file = open("output\output_top_cost_drug.txt", "a")
        file.write( "%s,%s,%s\n" % (g_keys[j[i][0]], cnt_per_drug[j[i][0]], j[i][1]))
file.close()

