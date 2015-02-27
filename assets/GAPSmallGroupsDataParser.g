LoadPackage( "sonata" );


NumberOfGAPSmallGroupsOfOrders := function( orders_list )

  return Sum( List( orders_list, order -> NumberSmallGroups( order ) ) );

  end;


NumberOfGAPSmallGroupsInIDRange := function( ID1, ID2)

  if ID1[1] in [1..2000] and ID2[1] in [1..2000] then
    if ID1[2] in [1..NumberSmallGroups( ID1[1] )] and
       ID2[2] in [1..NumberSmallGroups( ID2[1] )] then
      if ID1[1] < ID2[1] then
        return ( ( NumberSmallGroups( ID1[1] ) - ID1[2] + 1 ) +
               Sum( List( [ID1[1]+1..ID2[1]-1], order -> NumberSmallGroups( order ) ) ) +
               ID2[2] );
      elif ID1[1] = ID2[1] then
        return ( ID2[2] - ID1[2] + 1 );
      fi;
    fi;
  fi;

  return [];

  end;

NilpClass := function( G )

  if IsNilpotent( G ) then
    return NilpotencyClassOfGroup( G );
  else
    return "null";
  fi;

  end;


SolvableLength := function( G )

  if IsSolvable( G ) then
    return DerivedLength( G );
  else
    return "null";
  fi;

  end;


Generators := function( G )

  return List( GeneratorsOfGroup( G ), g -> [g,Order(g)] );

  end;


D3 := function( G )

  local x, DG;

  DG := 0;
  for x in CharacterDegrees( G ) do
    DG := DG + x[2]*( x[1]^3 );
  od;

  return DG;

  end;


IndexLargestAbelianNormalSubgroup := function( G )

  local li;

  li := List( Filtered( Subgroups( G ),
              H -> IsAbelian( H ) and IsNormal( G, H ) and Order( H ) > 1 ),
              K -> IndexNC( G, K ) );
  if li = [] then
    return "null";
  else
    return li[Length( li )];
  fi;

  end;


IndexLargestCyclicNormalSubgroup := function( G )

  local li;

  li := List( Filtered( Subgroups( G ),
              H -> IsCyclic( H ) and IsNormal( G, H ) and Order( H ) > 1 ),
              K -> IndexNC( G, K ) );
  if li = [] then
    return "null";
  else
    return li[Length( li )];
  fi;

  end;


IndexLargestElementaryAbelianNormalSubgroup := function( G )

  local li;

  li := List( Filtered( Subgroups( G ),
              H -> IsElementaryAbelian( H ) and IsNormal( G, H ) and Order( H ) > 1 ),
              K -> IndexNC( G, K ) );
  if li = [] then
    return "null";
  else
    return li[Length( li )];
  fi;

  end;


# GAP function for printing the JSON object information of a group in the GAP Small Groups # Library.

AsJSONObject := function( G )

  return Concatenation(
    "{\"GAP_ID\": ", String( IdSmallGroup( G ) ), ",",
     "\"GAP_desc\": \"", String( StructureDescription( G ) ), "\",",
     "\"GAP_pickled_ID\": ", "null", ",",
     "\"index_LAN_subgroup\": ", String( IndexLargestAbelianNormalSubgroup( G ) ), ",",
     "\"index_LCN_subgroup\": ", String( IndexLargestCyclicNormalSubgroup( G ) ), ",",
     "\"index_LEAN_subgroup\": ", String( IndexLargestElementaryAbelianNormalSubgroup( G ) ), ",",
     "\"is_abelian\": ", String( IsAbelian( G ) ), ",",
     "\"comm_length\": ", String( CommutatorLength( G ) ), ",",
     "\"is_cyclic\": ", String( IsCyclic( G ) ), ",",
     "\"is_elem_abelian\": ", String( IsElementaryAbelian( G ) ), ",",
     "\"is_simple\": ", String( IsSimple( G ) ), ",",
     "\"comp_length\": ", String( Size( CompositionSeries( G ) ) - 1 ), ",",
     "\"is_nilpotent\": ", String( IsNilpotent( G ) ), ",",
     "\"nilpotency_class\": ", String( NilpClass( G ) ), ",",
     "\"is_solvable\": ", String( IsSolvable( G ) ), ",",
     "\"derived_length\": ", String( SolvableLength( G ) ), ",",
     "\"is_pgroup\": ", String( IsPGroup( G ) ), ",",
     "\"generators\": \"", String( Generators( G ) ), "\",",
     "\"char_degrees\": \"", String( CharacterDegrees( G ) ), "\"}" );

  end;

excluded_TPP_small_groups := [ [128,[2320]],[192,[1541..1542]],[288,[1040,1044]],
                              [320,[1276..1640]],[324,[169,175]],
                              [384,[1336..20169]],[432],[448],
                              [480,[824..1213]],[486,[242..261]],
                              [512],[544],[576,[520..8681]],[640],
                              [648,[334..757]],[672,[684..1280]],
                              [686,[14]],[704,[487..1387]],[720,[473..840]],
                              [729,[122..504]],[736,[194]],[756,[172..189]],
                              [768],[784,[132..172]],[800,[218..1211]],
                              [810,[95..113]],[832,[298..1630]],
                              [880],[896],[900],[912],[928],[936],[960],[972],
                              [992],[1000] ];


ExceptionalTPPSmallGroupOrders := function()

  return List( excluded_TPP_small_groups, ex_group -> ex_group[1] );

  end;


IsExceptionalTPPSmallGroupOrder := function( order )

  return order in ExceptionalTPPSmallGroupOrders();

  end;


ExceptionalTPPSmallGroupIndicesOfOrder := function( order )

  local pos;

  pos := Position( ExceptionalTPPSmallGroupOrders(), order );
  if not pos = fail then
    if Length( excluded_TPP_small_groups[pos] ) = 1 then
      return [1..NumberSmallGroups( order )];
    else
      return excluded_TPP_small_groups[pos][2];
    fi;
  else
    return [];
  fi;

  end;


ExcludedTPPSmallGroupOrders := function()

  return List( Filtered( excluded_TPP_small_groups, ex_group -> Length( ex_group ) = 1 ),
               exc_group -> exc_group[1] );

  end;


IsExcludedTPPSmallGroupOrder := function( order )

  return order in ExcludedTPPSmallGroupOrders();

  end;


IsExcludedTPPSmallGroupID := function( ID )

  local pos;

  pos := Position( ExceptionalTPPSmallGroupOrders(), ID[1] );
  if not pos = fail then
    return ( ID[2] in excluded_TPP_small_groups[pos][2] );
  fi;

  return false;

  end;


WriteGAPSmallGroupsJSONFile := function( file_dir, file_name, ID1, ID2, inc_abelian, TPP_exclusions )

  local file, n, m, order, index, index_range, i, num_small_groups, G, total_groups, total_bytes;

  LoadPackage( "IO" );
  file := IO_File( Concatenation( file_dir, file_name ), "w" );
  total_groups := 0;
  total_bytes := 0;

  IO_WriteLine( file, "[" );
  n := ID1[1];
  m := ID2[1];
  for order in [n..m] do
    if n < m then
      if order = n then
        index_range := [ID1[2]..NumberSmallGroups( order )];
      elif order in [n+1..m-1] then
        index_range := [1..NumberSmallGroups( order )];
      elif order = m then
        index_range := [1..ID2[2]];
      fi;
    elif n = m then
      index_range := [ID1[2]..ID2[2]];
    fi;
    Print( "\n\torder=", order, ", initial index_range=", index_range );
    if TPP_exclusions = true then
      if not order in ExcludedTPPSmallGroupOrders() then
        index_range := Filtered( index_range,
                         index ->
                         not index in ExceptionalTPPSmallGroupIndicesOfOrder( order ) );
      else
        Print( "\n\t", order, " is excluded from TPP search!" );
        continue;
      fi;
    fi;
    Print( "\n\t(after TPP_exclusions) index_range=", index_range );
    for i in index_range do
      G := SmallGroup( order, i );
      if inc_abelian then
        if total_groups > 0 then
          total_bytes := total_bytes + IO_WriteLine( file, "," );
        fi;
        total_bytes := total_bytes + IO_Write( file, AsJSONObject( G ) );
        total_groups := total_groups + 1;
      else
        if not IsAbelian( G ) then
          if total_groups > 0 then
            total_bytes := total_bytes + IO_WriteLine( file, "," );
          fi;
          total_bytes := total_bytes + IO_Write( file, AsJSONObject( G ) );
          total_groups := total_groups + 1;
        fi;
      fi;
    od;
  od;
  total_bytes := total_bytes + IO_WriteFlush( file, "\n]" );

  IO_Close( file );

  Print( total_groups, " small groups successfully written as JSON objects to file ",
         Concatenation( file_dir, file_name ), " using ", Float( total_bytes / 1024 ),
         " Kb." );

  end;
