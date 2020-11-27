fn coloring(graph: &Vec<Vec<i32>>, max_color: i32) -> Vec<i32> {
    let mut color_map = vec![-1; graph.len()];
    if coloring_help(graph, &mut color_map, 0, max_color) {
        return color_map;
    }
    return vec![];
}

pub mod coloring_mod1 {
    pub fn eat() {}
}
fn coloring_help(
    graph: &Vec<Vec<i32>>,
    color_map: &mut Vec<i32>,
    index: usize,
    max_color: i32,
) -> bool {
    if index == graph.len() {
        return true;
    }
    for i in 0..max_color {
        if valid_color(graph, color_map, index, i) {
            color_map[index] = i;
            if coloring_help(graph, color_map, index + 1, max_color) {
                return true;
            }
            color_map[index] = -1;
        }
    }
    return false;
}

fn valid_color(graph: &Vec<Vec<i32>>, color_map: &Vec<i32>, index: usize, color: i32) -> bool {
    for i in 0..(graph.len()) {
        if graph[index][i] == 1 && color_map[i] == color {
            return false;
        }
    }
    return true;
}
pub fn coloring_test() {
    let graph = vec![
        vec![0, 1, 0, 0, 0],
        vec![1, 0, 1, 1, 1],
        vec![0, 1, 0, 1, 0],
        vec![0, 1, 1, 0, 0],
        vec![0, 1, 0, 0, 0],
    ];
    let v = coloring(&graph, 3);
    println!("{:?}", v);
}
