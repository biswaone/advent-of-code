num_pairs = 0
num_overlap_2 = 0

with open('advent-of-code-4.txt','r') as f:
    lines = f.read().split('\n')
    for x in lines:
        n1, n2 = x.split(',')[0].split('-')
        m1, m2 = x.split(',')[1].split('-')

        n1,n2,m1,m2 = int(n1),int(n2),int(m1),int(m2)

        if((n1<=m1 and n2>=m2) or (m1<=n1 and m2>=n2)):
            num_pairs += 1
        
        if((n1<=m1 and n2>=m2) or (n1>=m2 and n2<=m2) or (n1<=m2 and m1<=n2)) :
            num_overlap_2 += 1
        
    print(num_pairs)
    print(num_overlap_2)
        