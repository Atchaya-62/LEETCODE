class Solution {
    public int maxArea(int[] height) {
        int mx=0;
        int left=0;
        int right=height.length-1;
        while(left<right){
            
            final int water =Math.min(height[left],height[right]);
            mx=Math.max(mx,water*(right-left));
            if(height[left]<height[right]){
                ++left;
            }
            else{
                --right;
            }     
        }
        
    return mx;
    
}
}
