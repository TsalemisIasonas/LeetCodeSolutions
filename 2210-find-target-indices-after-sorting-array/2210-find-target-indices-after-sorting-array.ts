function targetIndices(nums: number[], target: number): number[] {
    const n = nums.length;
    let indices: number[] = [];

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (nums[j] < nums[i]) {
                const temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
        if (nums[i] === target) {
            indices.push(i);
        }
    }

    return indices;
    
};