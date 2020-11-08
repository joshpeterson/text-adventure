#include "hello.h"
#include "console.h"
#include "fmt/format.h"

using namespace fun;
using namespace fmt;

void hello(std::string name)
{
  console(format("Hello {}! :grinning face:", name));
}
