use std::io::stdin;
use std::str::FromStr;
use std::collections::{BinaryHeap, VecDeque};

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
    let q: usize = input_t();

    let mut hq: BinaryHeap<i64> = BinaryHeap::new();
    let mut que: VecDeque<usize> = VecDeque::new();

    for _ in 0..q {
        let qs: Vec<usize> = input_vec();
        match qs[..] {
            [1, x] => {
                que.push_back(x);
            },
            [2] => {
                match hq.pop() {
                    Some(x) => println!("--- {}", -x),
                    None => println!("--- {}", que.pop_front().unwrap()),
                }
            },
            [3] => {
                while !que.is_empty() {
                    hq.push(-(que.pop_front().unwrap() as i64));
                }
            },
            _ => unreachable!()
        }
    }
}
