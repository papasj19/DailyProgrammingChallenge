<?php



/**
 Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
 * @param Integer[] $nums
 * @return Integer
 */
function missingNumber($nums) {
    sort($nums);
    $prev = $nums[0];
    $start = 1;
    $size = sizeof($nums);
    while($start < $size){
        if($prev+1 == $nums[$start]){
            $prev = $nums[$start];
            $start++;
        }else{
            return $prev+1;
        }
    }
    return $size;
}
?>
