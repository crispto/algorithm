use std::collections::HashMap;
pub fn all_permutations(n: i32, k: i32) {
    let mut current_sequence: Vec<i32> = Vec::new();
    let mut map: HashMap<i32, bool> = HashMap::new();
    for i in 1..n + 1 {
        map.insert(i, false);
    }

    all_permutations_help(&mut current_sequence, n, k, &mut map);
}

fn all_permutations_help(tmp: &mut Vec<i32>, n: i32, k: i32, used: &mut HashMap<i32, bool>) {
    if tmp.len() as i32 == k {
        println!("{:?}", tmp);
    }
    for i in 1..n + 1 {
        let v = used.get(&i);
        match v {
            None => panic!("system failed"),
            Some(x) => {
                if *x {
                    continue;
                } else {
                    used.insert(i, true);
                    tmp.push(i);
                    all_permutations_help(tmp, n, k, used);
                    tmp.pop();
                    used.insert(i, false);
                }
            }
        }
    }
}
