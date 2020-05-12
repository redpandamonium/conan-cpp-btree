#include <btree/btree_set.h>
#include <cstdlib>

int main()
{
    btree::btree_set<int> s { };
    auto res = s.insert(5);
    if (!res.second) {
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
