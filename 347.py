'''
Top K Frequent Elements 

 Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''

        my_dict={}
        for i in nums:
            if i not in my_dict:
                my_dict[i]=1
            else:
                my_dict[i]+=1
            
        my_list=[]
        for i in range(k):
            temp= max(my_dict, key=my_dict.get)
            my_list.append(temp)
            my_dict.pop(temp,None)
        return my_list
        
