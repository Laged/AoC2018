use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn main() {
    let mut frequency = 0;
    let mut calibration_count = 0;
    let calibration_limit = 300;
    let mut calibrations = vec![frequency];
    loop {
        let f = File::open("input.txt").expect("file not found");
        let file = BufReader::new(&f);
        for line in file.lines() {
            let line_result = line.unwrap();
            let change: i32 = match line_result.trim().parse() {
                Ok(num) => num,
                Err(_) => continue,
            };
            frequency += change;
            // Second answer is found after iterating for a while...
            if calibrations.contains(&frequency) {
                println!("Answer to challenge #2: {}", frequency);
                return;
            }
            calibrations.push(frequency);
        }
        // First answer is found after first iteration
        if calibration_count == 0 {
            println!("Answer to challenge #1: {}", frequency);
            println!(
                "Running calibrations until {} to get answer #2, go get some coffee...",
                calibration_limit
            );
        }
        calibration_count += 1;
        // Stop iteration if limit is hit
        if calibration_count == calibration_limit {
            println!("Ended calibration loop without finding duplicates");
            return;
        }
    }
}
