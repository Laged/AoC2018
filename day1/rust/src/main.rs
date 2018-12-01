use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn main() {
    let f = File::open("input.txt").expect("file not found");
    let file = BufReader::new(&f);
    let mut frequency = 0;
    for line in file.lines() {
        let line_result = line.unwrap();
        let change: i32 = line_result.trim().parse().expect("Should be a number!");
        frequency += change;
    }
    println!("Answer to challenge #1: {}", frequency);
}
