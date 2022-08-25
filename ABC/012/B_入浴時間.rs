use std::io::stdin;
use std::str::FromStr;

fn input_t<T: FromStr>() -> T {
    let mut s: String = String::new();
    stdin().read_line(&mut s).ok().unwrap();
    s.trim().parse().ok().unwrap()
}

fn main() {
    let mut n: usize = input_t();
    let h = n / 3600;
    n -= h * 3600;
    let m = n / 60;
    n -= m * 60;
    let s = n;
    println!("{:0>2}:{:0>2}:{:0>2}", h, m, s);
}
