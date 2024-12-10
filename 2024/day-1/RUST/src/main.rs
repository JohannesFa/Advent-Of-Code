use std::fs;
//use std::env;

fn main() {
    let mut lines = fs::read_to_string("input.txt").expect("Read?");
    let line = lines.split("\n");
    
    for i in line{
        let nums = i.split("   ").collect::<Vec<_>>();
        let n1 = nums[0];
        let n2 = nums[1];
        println!("{}{}{}",i,n1,n2);
        
    }
    
}
