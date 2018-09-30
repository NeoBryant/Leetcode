class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        res=[]
        m=len(nums1)
        n=len(nums2)
        i1=0    #nums1的下标
        i2=0    #nums2的下标
        sum=m+n
        median=0

        if sum%2==0: #总数为偶数
            for i in range((sum//2)+1):
                if nums1[i1]<nums2[i2]:
                    if i>=(sum//2)-1:
                        median+=nums1[i1]
                    
                else:
                    if i>=(sum//2)-1:
                        median+=nums2[i2]
                    i2+=1
            return median/2

        else:
            for i in range((sum//2)+1):
                if nums1[i1]<nums2[i2]:
                    i1+=1
                    if i==(sum//2):
                        median=nums1[i1]
                else:
                    i2+=1
                    if i==sum//2:
                        median=nums2[i2]
            return median*1.0
        
a=Solution()
n1=[1,2]
n2=[3,4]
b=a.findMedianSortedArrays(n1,n2)
print(b)