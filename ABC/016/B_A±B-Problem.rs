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
    let v: Vec<usize> = input_vec();
    let (a, b, c): (usize, usize, usize) = (v[0], v[1], v[2]);


    if a + b == c && a - b == c {
        println!("?");
    } else if a + b == c {
        println!("+");
    } else if a - b == c {
        println!("-");
    } else {
        println!("!");
    }
}