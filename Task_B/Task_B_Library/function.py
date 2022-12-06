def comparator_versions(v1: str, v2: str):
  """
  Calculate wether two versions of the same library are 
  greather than, equal or less than the other.

  Args:
    v1(string): version of a library
    v2(string): version of a library 

  Returns:
    string: The return value is a string. The string contains one case string, 
    according to the comparison of the version number:
      case 1 return: version v1 is greater than version v2  
      case 2 return: version v1 is less than version v2 
      case 3 return: version v1 is equal to version v2 
  
  
  Example:
    The following code will perform a comparison of two version numbers. 
    To do that requires two strings inputs containing a library's version numbers. 
    The code has 3 return cases however it has 5 input cases that were taken 
    into account to perform comparison versioning.


      Case 1:
    
        >>> print(comparator_versions("1.20.1", "0.5.1"))
        version 1.20.1 is greater than version 0.5.1
    
      Case 2:
    
        >>> print(comparator_versions("1.20.1", "4.5.1"))
        version 1.20.1 is less than version 4.5.1
    
     Case 3:
    
        >>> print(comparator_versions("1.20.1", "1.20.1"))
        version 1.20.1 is equal to version 1.20.1
    
      Case 4:
    
        >>> print(comparator_versions("1.20", "1.20.1"))  
        version 1.20 is less than version 1.20.1
    
     Case 5:
    
        >>> print(comparator_versions("1.20.1.10", "1.20.1"))
        version 1.20.1.10 is greater than version 1.20.1

  Raises:
    ValueError: If `v1` type is different to `str`.
    ValueError: If `v2` type is different to `str`.

  """
  if type(v1) != str:
    raise ValueError('v1 type must be equal to str')
  
  if type(v2) != str:
    raise ValueError('v2 type must be equal to str')

  #Change wrong separation for major.minor.patch format version. Example: 1,20.1 to 1.20.1
  if v1.find(',')==1:
    v1 = v1.replace(",", ".")

  if v2.find(',')==1:
    v2 = v2.replace(",", ".")

  
  v1_lst = v1.split(".")
  v2_lst = v2.split(".")

  v1_lst = [int(i) for i in v1_lst]
  v2_lst = [int(i) for i in v2_lst]

  n = len(v1_lst)
  m = len(v2_lst)

  if n>m:
    for i in range(m, n):
     v2_lst.append(0)
  elif m>n: 
     for i in range(n, m):
       v1_lst.append(0)
  for i in range(len(v1_lst)):
    if v1_lst[i]>v2_lst[i]:
      string  = 'version %s is greater than version %s'  %(v1, v2)
      return string
    elif v2_lst[i]>v1_lst[i]:
      string  ='version %s is less than version %s'  %(v1, v2)
      return string
  string  = 'version %s is equal to version %s'  %(v1, v2)    
  return string