use std::io::stdin;
use std::str::FromStr;

fn input_t<T: FromStr>() -> T {
    let mut s: String = String::new();
    stdin().read_line(&mut s).ok().unwrap();
    s.trim().parse().ok().unwrap()
}

fn input_vec<T: FromStr>() -> Vec<T> {
    input_t::<String>()
        .split_whitespace()
        .map(|e| e.parse().ok().unwrap())
        .collect()
}

fn main() {
    let xy: Vec<i32> = input_vec();
    let x: i32 = xy[0];
    let y: i32 = xy[1];

    if (x - y).abs() <= 2 {
        println!("Yes");
    } else {
        println!("No");
    }
}